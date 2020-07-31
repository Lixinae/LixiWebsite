import concurrent.futures
import requests
from flask import render_template, make_response, request, send_file, after_this_request, jsonify
from flask_restx import Resource
from backend.apps.webcrawler import webcrawler_api, webcrawler_source, webcrawler_toolbox, logger
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


@webcrawler_api.route('/')
class WebcrawlerPage(Resource):
    def get(self):
        webcrawler_html = "webcrawler.html"
        return make_response(render_template(webcrawler_html), 200)

    def post(self):
        errors = []
        webcrawler_html = "webcrawler.html"
        results = {}
        base_url = ""
        try:
            base_url = request.form['url']
            logger.info("Requesting url : " + base_url)
            if not webcrawler_toolbox.link_check(base_url):
                errors.append(
                    "Unable to get URL. Please make sure it's valid and try again."
                )
                logger.error("Url : " + base_url + " is invalid")
                return make_response(render_template(webcrawler_html, errors=errors), 200)
            resquest_result = requests.get(base_url)
            logger.debug("Request on url : " + base_url + " worked")
        except:
            url_is_invalid = "Url : " + base_url + " is invalid"
            logger.error(url_is_invalid)
            errors.append(url_is_invalid)
            return make_response(render_template(webcrawler_html, errors=errors), 200)
        if resquest_result:
            domain = base_url.split("/")[2]
            extensions_string = request.form['extensions']
            extensions = []
            if extensions_string:
                extensions_string = extensions_string.replace(" ", "")
                extensions = extensions_string.split(";")
            depth = int(request.form['depth'])
            debug_message = "Parameters are : \n" + "Domain: " + domain + "\n" + "Extensions: " + ",".join(
                extensions) + "\n" + "Depth: " + str(depth)
            logger.debug(debug_message)
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


def webcrawler_download_annexe(download_folder: str):
    webcrawler_source.download_all(download_links)
    return webcrawler_toolbox.zipdir(download_folder)


@webcrawler_api.route('/api/webcrawlerDownload')
class WebcrawlerDownload(Resource):
    def get(self):
        pass

    def post(self):
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
