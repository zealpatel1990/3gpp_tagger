import json


def get_text_from_file(input_file):
    with open(input_file, 'r') as f:
        text_content = f.read()
        f.close()
    return text_content


def write_text_to_file(text, file_name):
    with open(file_name, 'w') as f:
        f.write(text)
        f.close()


def write_json_to_file(dict_value, file_name):
    with open(file_name, 'w') as f:
        json.dump(dict_value, f, indent=6)
        f.close()
