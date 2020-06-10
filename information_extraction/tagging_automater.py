from utils.path_finder import resolve_path_from_project_dir
import json


class AutoTagProcessor:
    def __init__(self, input_text):
        self.input = input_text
        self.rules_config = json.load(open(resolve_path_from_project_dir('configs/rules.json')))
        self.priority_configs = json.load(open(resolve_path_from_project_dir('configs/processing_priority.json')))

    def tag_words(self):
        print(self.rules_config)
        print(self.priority_configs)


if __name__ == '__main__':
    auto_tag_processor = AutoTagProcessor(resolve_path_from_project_dir('configs/input_data.txt'))
    auto_tag_processor.tag_words()
