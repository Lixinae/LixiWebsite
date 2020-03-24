# -*- coding: cp1252 -*-
# !/usr/bin/python

import os
import re
import sys

import requests
from typing import List, Optional, Match

import urllib.request as urllib2
import urllib.parse as urlparse

try:
    import bs4

    print("BeautifulSoup4 is there, starting program")
except ImportError:
    print("BeautifulSoup4 not installed, please install before using the script")
    print("Instructions in README file")
    print("Leaving program")
    sys.exit(1)


# Format du dictionnaire pour 1 lien#
# {
#     'link':"liensVersRessource",
#     'name':"nomDeRessource",
#     'isVisited':True # Ou false, si le lien a d�j� �t� visit� ou non pendant le parcours
# }

# Evite les erreurs de unicode
# Bug parfois
# FromRaw = lambda r: r if isinstance(r, unicode) else r.decode('utf-8', 'ignore')

# Security checks for the link provided
def security_check(link: str,
                   depth: int,
                   dict_links,  #: List[Dict[str, str, bool]],
                   domain: str) -> bool:
    # Checks the depth we are at
    if depth <= 0:
        return False
    # Checks if there is to much links in the dictionnary
    if len(dict_links) > 10000:
        print("Too much links in list -> stoping crawling")
        return False
    # Checks if the provided link is correct
    if not link_check(link):
        return False
    # Checks if the link is in the base domain
    if not has_domain(link, domain):
        return False
    # Checks if the link is already in the dictionnary and if has been visited
    link_in_dictionnary = next((item for item in dict_links if item["link"] == link), None)
    print(link_in_dictionnary)
    if link_in_dictionnary:
        if link_in_dictionnary["isVisited"]:
            return False
    return True


# Constructs the links dictionnary
# On ne pas �crire "List[Dict[str, str, bool]]" pour le typing -> Erreur au lancement
def construct_tree_link(base_link: str,
                        depth: int,
                        dict_links,  #: List[Dict[str, str, bool]],
                        domain: str,
                        extensions: List[str]):  # -> List[Dict[str, str, bool]]:
    if not security_check(base_link, depth, dict_links, domain):
        return []
    try:
        page = urllib2.urlopen(base_link)
    except Exception:
        print("Could not open link :" + base_link)
        return []
    # Tels if we already visited the link
    # Plus logique ici que dans la boucle
    file_name = base_link.split('/').pop()
    if any([ext for ext in extensions if base_link.endswith(ext)]):
        dict_link = {"link": base_link, "name": file_name, "isVisited": False}
        dict_links.append(dict_link)

    read = page.read()
    # read = FromRaw(read)
    soup = bs4.BeautifulSoup(read, "html.parser")
    links_a = soup.findAll("a")
    for linkA in links_a:
        clean_string = urlparse.unquote(linkA.get('href', '/'))
        download_link = urlparse.urljoin(base_link, clean_string)
        # Checks if we do not go back in the website
        if not len(download_link) < len(base_link):
            # Avoid strange links
            if "?" not in download_link:
                if download_link not in dict_links:
                    download_link = re.sub(r"[\t\n]", "", download_link)
                    # Add the link to the dictionnary, indicating it's not yet visited
                    file_name = download_link.split('/').pop()
                    if any([ext for ext in extensions if download_link.endswith(ext)]):
                        dict_link = {"link": download_link, "name": file_name, "isVisited": False}
                        dict_links.append(dict_link)
                construct_tree_link(download_link, depth - 1, dict_links, domain, extensions)
                # Tels if we already visited the link
                # dictLinks[downloadLink] = True
    return dict_links


# Downloads everything in the links provided
# On ne pas �crire "List[Dict[str, str, bool]]" pour le typing -> Erreur au lancement
def download_all(links):
    pattern_filename = re.compile('(\w+)(\.\w+)+(?!.*(\w+)(\.\w+)+)$')
    folder = "default"
    folder_download = "download"
    create_folder(folder_download)
    for link_dict in links:
        name = link_dict["name"]
        link = link_dict["link"]
        if pattern_filename.search(name):
            m = re.search("http:\/\/(.*\/)", link)
            if m:
                folder = m.group(1)
            create_folder(folder_download + "/" + folder)
            print(link)
            r = requests.get(link, stream=True)
            with open(folder_download + "/" + folder + "/" + name, "wb") as f:
                for chunk in r:
                    f.write(chunk)
                    f.flush()


# If a folder doesn't exist, it's created
def create_folder(name):
    if not os.path.exists(name):
        print("Creating folder " + name)
        os.makedirs(name)


# Verify if the given url is in the start domain
def has_domain(url, test_domain) -> bool:
    return urlparse.urlparse(url).hostname in test_domain


# Tests if the link provided is a correct url
# Regexp made by @dperini ported by @adamrofer on github
def link_check(link: str) -> Optional[Match[str]]:
    return re.search(re.compile(
        u"^"
        # protocol identifier
        u"(?:(?:https?|ftp)://)"
        # user:pass authentication
        u"(?:\S+(?::\S*)?@)?"
        u"(?:"
        # IP address exclusion
        # private & local networks
        u"(?!(?:10|127)(?:\.\d{1,3}){3})"
        u"(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})"
        u"(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})"
        # IP address dotted notation octets
        # excludes loopback network 0.0.0.0
        # excludes reserved space >= 224.0.0.0
        # excludes network & broadcast addresses
        # (first & last IP address of each class)
        u"(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])"
        u"(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}"
        u"(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))"
        u"|"
        # host name
        u"(?:(?:[a-z\u00a1-\uffff0-9]-?)*[a-z\u00a1-\uffff0-9]+)"
        # domain name
        u"(?:\.(?:[a-z\u00a1-\uffff0-9]-?)*[a-z\u00a1-\uffff0-9]+)*"
        # TLD identifier
        u"(?:\.(?:[a-z\u00a1-\uffff]{2,}))"
        u")"
        # port number
        u"(?::\d{2,5})?"
        # resource path
        u"(?:/\S*)?"
        u"$"
        , re.UNICODE), link)
