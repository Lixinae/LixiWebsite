import concurrent.futures
import threading
import time
import zipfile
from io import BytesIO
from typing import Dict

from flask import render_template, make_response, request, send_file

from application.webcrawler import webcrawler_bp, webcrawlerSource

import requests
import bs4

# Necessaire pour avoir les info au moment du submit
download_links = {}


############################################
#              WebCrawler                  #
############################################

def web_crawler_parse_website(base_url: str, domain: str, depth: int) -> Dict[str, bool]:
    return webcrawlerSource.construct_tree_link(base_url, depth, download_links, domain)


@webcrawler_bp.route("/webcrawler", methods=['GET', 'POST'])
def web_crawler():
    errors = []
    results = {}
    if request.method == "POST":
        # Todo -> Avoir les info sous forme de formulaire
        try:
            base_url = request.form['url']
            if not webcrawlerSource.link_check(base_url):
                errors.append(
                    "Unable to get URL. Please make sure it's valid and try again."
                )
                return make_response(render_template("webcrawler.html", errors=errors), 200)
            r = requests.get(base_url)
        except:
            errors.append(
                "Unable to get URL. Please make sure it's valid and try again."
            )
            return make_response(render_template("webcrawler.html", errors=errors), 200)
        if r:
            domain = base_url.split("/")[2]
            extensions_string = request.form['extensions']
            extensions_string = extensions_string.replace(" ", "")
            extensions = extensions_string.split(";")
            depth = int(request.form['depth'])
            # Afin de ne pas paralyser le serveur, on fera la recolte des liens dans un thread à part
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(web_crawler_parse_website, base_url, domain, depth)
                results = future.result()
                global download_links
                download_links = results
    return make_response(render_template("webcrawler.html", results=results), 200)


def web_crawler_download_annexe():
    pass
    # memory_file = BytesIO()
    # with zipfile.ZipFile(memory_file, 'w') as zf:
    #     files = result['files']
    #     for individualFile in files:
    #         data = zipfile.ZipInfo(individualFile['fileName'])
    #         data.date_time = time.localtime(time.time())[:6]
    #         data.compress_type = zipfile.ZIP_DEFLATED
    #         zf.writestr(data, individualFile['fileData'])
    # memory_file.seek(0)
    # return memory_file


@webcrawler_bp.route("/webcrawlerDownload", methods=['POST'])
def web_crawler_download():
    pass
    # Afin de ne pas paralyser le serveur, on fera le téléchargement des liens dans un thread à part
    # Todo
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(web_crawler_download_annexe)
        memory_file = future.result()
        print(memory_file)
        return send_file(memory_file, attachment_filename='files.zip', as_attachment=True)
