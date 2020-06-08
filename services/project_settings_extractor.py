import requests
import json
from utils.path_finder import resolve_path_from_project_dir
from requests.auth import HTTPBasicAuth


def get_project_setting():
    qualified_config_file = resolve_path_from_project_dir('configs/service_configuration.json')
    with open(qualified_config_file, 'r') as f:
        service_configuration = json.load(f)
        f.close()

    for each in service_configuration:
        if each['api'] == 'get_project_setting':
            service = each
            break
    result = requests.get(url=service['endpoint'], params=service['params'],
                          auth=HTTPBasicAuth(service['username'], service['password']))

    entities_json = resolve_path_from_project_dir('configs/entity_configuration.json')
    data = result.json()['entities']
    with open(entities_json, 'w') as f:
        json.dump(data, f, indent=4, sort_keys=True)
        f.close()

