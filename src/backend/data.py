import json
import os

from src.backend import constants as cnst


def dump_data_json(data, name):
    data_folder()
    path = cnst.DATA_PATH + name + '.json'
    with open(path, 'w') as f:
        json.dump(data, f)


def load_data(name):
    data_folder()
    path = cnst.DATA_PATH + name + '.json'
    with open(path, 'r') as f:
        return json.load(f)


def delete_file(file_name):
    file_path = cnst.DATA_PATH + file_name + '.json'
    os.remove(file_path)


def data_folder():
    if not os.path.exists(cnst.DATA_PATH):
        os.makedirs(cnst.DATA_PATH)


def is_file_present(file_name):
    return os.path.exists(cnst.DATA_PATH + file_name + '.json')
