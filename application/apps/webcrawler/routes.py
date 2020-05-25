import concurrent.futures
import requests
from flask import render_template, make_response, request, send_file, after_this_request, jsonify

from application.apps.webcrawler import webcrawler_bp, webcrawler_source, webcrawler_toolbox, logger
import json

# Necessaire pour avoir les info au moment du submit
download_links = []


# Format du dictionnaire pour 1 lien#
# {
#     'link':"liensVersRessource",
#     'name':"nomDeRessource",
#     'isVisited':True # Ou false, si le lien a déjà été visité ou non pendant le parcours
# }

############################################
#              WebCrawler                  #
############################################

# On ne pas écrire "List[Dict[str, str, bool]]" pour le typing -> Erreur au lancement
# Parse le site web et récupère les liens
def webcrawler_parse_website(base_url: str, domain: str, depth: int, extensions):  # -> List[Link]:
    global download_links
    download_links = []
    logger.debug("Starting crawling")
    list_link = webcrawler_source.construct_tree_link(base_url, depth, download_links, domain, extensions)
    unique_ordered_links = webcrawler_toolbox.keep_unique_ordered(list_link)
    logger.debug("End of crawling : list of links : %s", unique_ordered_links)
    return unique_ordered_links


@webcrawler_bp.route("/", methods=['GET', 'POST'])
def webcrawler():
    errors = []
    webcrawler_html = "webcrawler.html"
    if request.method == "POST":
        results = {}
        unable_to_get_url = "Unable to get URL. Please make sure it's valid and try again."
        try:
            base_url = request.form['url']
            if not webcrawler_toolbox.link_check(base_url):
                errors.append(
                    unable_to_get_url
                )
                return make_response(render_template(webcrawler_html, errors=errors), 200)
            r = requests.get(base_url)
        except:
            errors.append(unable_to_get_url)
            logger.error(unable_to_get_url)
            return make_response(render_template(webcrawler_html, errors=errors), 200)
        if r:
            domain = base_url.split("/")[2]
            extensions_string = request.form['extensions']
            extensions = []
            if extensions_string:
                extensions_string = extensions_string.replace(" ", "")
                extensions = extensions_string.split(";")
            depth = int(request.form['depth'])
            # Ne devrait jamais arriver
            if depth <= 0:
                errors.append("Received depth is < or = to 0 -> No crawling")
                return make_response(render_template(webcrawler_html, errors=errors), 200)
            # Afin de ne pas paralyser le serveur, on fera la recolte des liens dans un thread à part
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(webcrawler_parse_website, base_url, domain, depth, extensions)
                results = future.result()
                global download_links
                download_links = results
        if results:
            result_as_list_json = [r.as_json() for r in results]
            logger.debug("Return results : %s", "".join([json.dumps(res) for res in result_as_list_json]))
            return jsonify({"results": result_as_list_json})
    return make_response(render_template(webcrawler_html), 200)


def webcrawler_download_annexe(download_folder: str):
    webcrawler_source.download_all(download_links)
    return webcrawler_toolbox.zipdir(download_folder)


@webcrawler_bp.route("/api/webcrawlerDownload", methods=['POST'])
def webcrawler_download():
    download_folder = "./download"
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(webcrawler_download_annexe, download_folder)
        memory_file = future.result()

        @after_this_request
        def remove_file(response):
            logger.debug("Removing temporary folder : %s", download_folder)
            webcrawler_toolbox.remove_directory_and_all_files_in(download_folder)
            return response

        logger.debug("Send zip file folder : %s", "files.zip")
        return send_file(memory_file, attachment_filename='files.zip', as_attachment=True)
