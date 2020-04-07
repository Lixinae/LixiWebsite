import os
import zipfile
import shutil
from io import BytesIO
from typing import List, Optional, Match
from application.apps.webcrawler import regexp_patterns


# Cré un zip ayant à partir du dossier "path", et du fichier zip "ziph" créer précédemment
def zipdir(path: str):
    memory_file = BytesIO()
    with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(path):
            for file in files:
                zipf.write(os.path.join(root, file))
    memory_file.seek(0)
    return memory_file
    # ziph is zipfile handle


# Renvoie la liste de tous les chemins des fichiers dans le dossier "path"
def list_files_from_path(path: str) -> List[str]:
    files_list = []
    for root, directories, files in os.walk(path):
        for file in files:
            files_list.append(os.path.join(root, file))
    return files_list


# Supprime le dossier "dir_path" et tout les fichiers qu'il contient
def remove_directory_and_all_files_in(dir_path: str):
    try:
        shutil.rmtree(dir_path)
    except OSError as e:
        print("Error: %s : %s" % (dir_path, e.strerror))


# Keeps the distinct elements in a list, in the same order as the start
def keep_unique_ordered(my_list) -> List:
    return [x for i, x in enumerate(my_list) if x not in my_list[:i]]


# Tests if the link provided is a correct url
# Regexp made by @dperini ported by @adamrofer on github
def link_check(link: str) -> Optional[Match[str]]:
    return regexp_patterns.pattern_valid_url.search(link)


# If a folder doesn't exist, it's created
def create_folder(name):
    if not os.path.exists(name):
        print("Creating folder " + name)
        os.makedirs(name)
