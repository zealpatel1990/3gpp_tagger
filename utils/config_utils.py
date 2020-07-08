from utils.path_finder import resolve_path_from_project_dir
import json


def get_class_from_name(input_name):
    entity_config = json.load(open(resolve_path_from_project_dir('configs/entity_configuration.json')))
    for (key, value) in entity_config.items():
        if value['name'] == input_name:
            return key


def get_index(value, input_list):
    try:
        index_value = input_list.index(value)
    except ValueError:
        index_value = -1
    return index_value
