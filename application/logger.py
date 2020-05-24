import logging
import logging.config
import os

import yaml
from pathlib import Path


def setup_logging():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_parent_path = Path(dir_path).parent
    path = os.path.join(dir_parent_path, "loggingConfig.yaml")
    # Creation du dossier pour les logs dans le cas ou il n'existe pas
    try:
        os.mkdir(os.path.join(dir_parent_path, "logs"))
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)
    with open(path, 'rt') as file:
        config = yaml.safe_load(file.read())
        logging.config.dictConfig(config)
