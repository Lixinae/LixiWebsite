import os
from typing import List
import shutil


# Cré un zip ayant pour nom "ziph" à partir du dossier "path"
def zipdir(path: str, ziph: str):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


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
def keep_unique_ordered(my_list):
    return [x for i, x in enumerate(my_list) if x not in my_list[:i]]
