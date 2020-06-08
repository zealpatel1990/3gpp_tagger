import os

abs_project_path = os.path.abspath(os.path.join(os.getcwd(), '../'))


def resolve_path_from_project_dir(input_value):
    return os.path.join(abs_project_path, input_value)

