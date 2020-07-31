import os
import zipfile
import shutil
from io import BytesIO
from typing import List, Optional, Match
from application.apps.webcrawler import regexp_patterns


def zipdir(path: str) -> BytesIO:
    """
    Create a zip file from the folder "path", and return the data to be sent
    :param path: Folder from which the zipfile is created
    :return: The memory_file created
    """
    memory_file = BytesIO()
    with zipfile.ZipFile(memory_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(path):
            for file in files:
                zipf.write(os.path.join(root, file))
    memory_file.seek(0)
    return memory_file


def list_files_from_path(path: str) -> List[str]:
    """
    Returns the list of the files in the given folder (including subfolders),
    :param path: Folder where to look
    :return: The list of the files in the given folder (including subfolders)
    """
    files_list = []
    for root, directories, files in os.walk(path):
        for file in files:
            files_list.append(os.path.join(root, file))
    return files_list


def remove_directory_and_all_files_in(dir_path: str):
    """
    Deletes the folder 'dir_path' and all it's content
    :param dir_path: Folder to delete and all it's content
    """
    try:
        shutil.rmtree(dir_path)
    except OSError as e:
        print("Error: %s : %s" % (dir_path, e.strerror))


# Keeps the distinct elements in a list, in the same order as the start
def keep_unique_ordered(my_list: List) -> List:
    """
    Keeps only 1 element of each in the list, keeping the order
    :param my_list: List you want to parse
    :return: A list with only unique element, keeping the order of the previous list
    """
    return [x for i, x in enumerate(my_list) if x not in my_list[:i]]


# Tests if the link provided is a correct url
def link_check(link: str) -> Optional[Match[str]]:
    """
    Checks if the givin link is a valid url
    :param link: The link to check
    :return: True if valid, False otherwise
    """
    return regexp_patterns.pattern_valid_url.search(link)


# If a folder doesn't exist, it's created
def create_folder(name: str):
    """
    Creates the folder "name" if it doesn't exist
    :param name: The path to the folder you are creating
    """
    if not os.path.exists(name):
        print("Creating folder " + name)
        os.makedirs(name)
