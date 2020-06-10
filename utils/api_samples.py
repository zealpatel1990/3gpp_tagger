import requests

from utils.file_utils import get_text_from_file
from utils.path_finder import resolve_path_from_project_dir


def upload_verbatim_text():
    tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

    content = get_text_from_file(resolve_path_from_project_dir('configs/input_data.txt'))

    auth = requests.auth.HTTPBasicAuth(username="charantej", password="Password*01")
    params = {"project": "tagging_project", "owner": "charantej", "format": "verbatim", "output": "null"}
    payload = {
        "text": content
    }
    response = requests.post(tagtogAPIUrl, params=params, auth=auth, data=payload)


def verbatim_annotate():
    tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

    auth = requests.auth.HTTPBasicAuth(username="charantej", password="Password*01")
    params = {"project": "tagging_project", "owner": "charantej", "format": "verbatim-plus-annjson",
              "output": "null"}

    files = [
        ("input_data.txt", open(resolve_path_from_project_dir('configs/input_data.txt'))),
        ("input_data.ann.json", open(resolve_path_from_project_dir('configs/verb_ann.json')))
    ]
    response = requests.post(tagtogAPIUrl, params=params, auth=auth, files=files)
    print(response.text)


if __name__ == '__main__':
    verbatim_annotate()
