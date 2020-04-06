import os
import zipfile
from io import BytesIO
from typing import List
import shutil


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
