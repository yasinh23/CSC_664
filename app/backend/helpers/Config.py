import io
import os
import json
from app.constants import ROOT_DIR


def config_exists(path):
    path = path
    if os.path.exists(path):
        return True
    return False


def create_config(path):
    f = open(f"{path}", "a")
    return f


def load_config(s):
    """
    :param s: config file plain text
    :return dict: config file as dictionary if file is populated; empty dict if not
    """
    try:
        return json.load(s)
    except io.UnsupportedOperation:
        return dict()


def write_config(f, j):
    f.write(json.dumps(j))
    f.close()


def get_gallery_dir():
    f = open(f"{ROOT_DIR}/.config", "r")
    d = load_config(f)
    return d['gallery_folder']
