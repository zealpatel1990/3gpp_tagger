from requests.auth import HTTPBasicAuth
import json

from utils.path_finder import resolve_path_from_project_dir


def get_auth_params(service_config_dict):
    return HTTPBasicAuth(service_config_dict['username'], service_config_dict['password']), service_config_dict[
        'params'], service_config_dict['endpoint']


def get_service_config(input_key):
    qualified_config_file = resolve_path_from_project_dir('configs/service_configuration.json')
    with open(qualified_config_file, 'r') as f:
        service_config = json.load(f)
        f.close()
    for each in service_config:
        if each['api'] == input_key:
            service = each
    return service
