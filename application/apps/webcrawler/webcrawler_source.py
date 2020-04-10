# -*- coding: cp1252 -*-
# !/usr/bin/python

import os
import re
import bs4

import requests
from typing import List

import urllib.request as urllib2
import urllib.parse as urlparse

from application.apps.webcrawler import regexp_patterns
from application.apps.webcrawler.webcrawler_link import LinkEnum, Link
from application.apps.webcrawler.webcrawler_toolbox import create_folder, link_check


# Evite les erreurs de unicode
# Bug parfois
# FromRaw = lambda r: r if isinstance(r, unicode) else r.decode('utf-8', 'ignore')

# Security checks for the link provided
def security_check(link: str,
                   depth: int,
                   list_links: List[Link],  #: List[Dict[str, str, bool]], # List[Link]
                   domain: str) -> bool:
    # Checks the depth we are at
    if depth <= 0:
        return False
    # Checks if there is to much links in the dictionnary
    if len(list_links) > 10000:
        print("Too much links in list -> stoping crawling")
        return False
    # Checks if the provided link is correct
    if not link_check(link):
        return False
    # Checks if the link is in the base domain
    if not has_domain(link, domain):
        return False
    # Checks if the link is already in the dictionnary and if has been visited
    link_in_dictionnary = next((item for item in list_links if item.get_url() == link), None)
    if link_in_dictionnary:
        if link_in_dictionnary.is_visited():
            return False
    return True


# Parsing des balises "a"
def parse_all_a(soup,
                base_url: str,
                list_links: List[Link],
                extensions: List[str],
                depth: int,
                domain: str):
    links_a = soup.findAll("a")
    for linkA in links_a:
        clean_string = urlparse.unquote(linkA.get('href', '/'))
        download_url = urlparse.urljoin(base_url, clean_string)
        # Checks if we do not go back in the website
        if not len(download_url) < len(base_url):
            # Avoid strange links
            if "?" not in download_url:
                add_to_list_link(download_url, extensions, list_links, LinkEnum.AHref)
                construct_tree_link(download_url, depth - 1, list_links, domain, extensions)


# Parsing des balises "img"
def parse_all_img(soup,
                  base_url: str,
                  list_links: List[Link],
                  extensions: List[str]):
    links_img = soup.find_all("img")
    for linkA in links_img:
        clean_string = urlparse.unquote(linkA.get('src', '/'))
        download_url = urlparse.urljoin(base_url, clean_string)
        add_to_list_link(download_url, extensions, list_links, LinkEnum.Img)


# Ajout d'un lien a la liste des liens à télécharger
def add_to_list_link(download_url: str,
                     extensions: List[str],
                     list_links: List[Link],
                     link_enum: LinkEnum):
    if download_url not in [x.get_url() for x in list_links]:
        download_url = re.sub(r"[\t\n]", "", download_url)
        if extensions:
            # Add the link to the dictionnary, indicating it's not yet visited
            if any([ext for ext in extensions if download_url.endswith(ext)]):
                dict_link = Link(download_url, link_enum)
                list_links.append(dict_link)
        else:
            dict_link = Link(download_url, link_enum)
            name = dict_link.get_name()
            if regexp_patterns.pattern_filename.search(name) and not regexp_patterns.pattern_email.search(name):
                list_links.append(dict_link)


# Constructs the links dictionnary
# On ne pas écrire "List[Dict[str, str, bool]]" pour le typing -> Erreur au lancement
def construct_tree_link(base_url: str,
                        depth: int,
                        list_links: List[Link],  #: List[Dict[str, str, bool]], # List[Link]
                        domain: str,
                        extensions: List[str]):  # -> List[Dict[str, str, bool]]:
    if not security_check(base_url, depth, list_links, domain):
        return []
    try:
        page = urllib2.urlopen(base_url)
    except Exception:
        print("Could not open link :" + base_url)
        return []
    # Tels if we already visited the link
    # Plus logique ici que dans la boucle
    dict_link = next((item for item in list_links if item.get_url() == base_url), None)
    if dict_link:
        dict_link.set_visited()

    read = page.read()
    # read = FromRaw(read)
    soup = bs4.BeautifulSoup(read, "html.parser")

    # Parse des balises img
    parse_all_img(soup, base_url, list_links, extensions)

    # Parse des liens "a"
    parse_all_a(soup, base_url, list_links, extensions, depth, domain)
    return list_links


# Downloads everything in the links provided
# On ne pas écrire "List[Dict[str, str, bool]]" pour le typing -> Erreur au lancement
def download_all(links):
    folder = "default"
    folder_download = "download"
    create_folder(folder_download)
    for link_dict in links:
        name = link_dict.get_name()
        url = link_dict.get_url()
        if regexp_patterns.pattern_filename.search(name):
            m = re.search("http:\/\/(.*\/)", url)
            if m:
                folder = m.group(1)
                # Les ":" ne sont pas permis dans un nom de dossier
                folder = folder.replace(":", "_")
            create_folder(folder_download + "/" + folder)
            r = requests.get(url, stream=True)
            with open(folder_download + "/" + folder + "/" + name, "wb") as f:
                for chunk in r:
                    f.write(chunk)
                    f.flush()


# Verify if the given url is in the start domain
def has_domain(url: str, domain: str) -> bool:
    return urlparse.urlparse(url).hostname in domain
