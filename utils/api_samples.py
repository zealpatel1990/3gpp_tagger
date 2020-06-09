import requests

from utils.file_utils import get_text_from_file
from utils.path_finder import resolve_path_from_project_dir

tagtogAPIUrl = "https://www.tagtog.net/-api/documents/v1"

content = get_text_from_file(resolve_path_from_project_dir('configs/input_data.txt'))

auth = requests.auth.HTTPBasicAuth(username="charantej", password="Password*01")
params = {"project": "tagging_project", "owner": "charantej", "format": "verbatim", "output": "null"}
payload = {
    "text": content
}
print(tagtogAPIUrl)
print(params)
print(auth)
print(payload)
response = requests.post(tagtogAPIUrl, params=params, auth=auth, data=payload)
print(response.text)
