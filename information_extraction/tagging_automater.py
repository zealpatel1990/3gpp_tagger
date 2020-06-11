from utils.path_finder import resolve_path_from_project_dir
import json


class AutoTagProcessor:
    def __init__(self, input_text, target_name):
        self.target_name = target_name
        self.input = input_text
        self.rules_config = json.load(open(resolve_path_from_project_dir('configs/rules.json')))
        self.priority_configs = json.load(open(resolve_path_from_project_dir('configs/processing_priority.json')))
        self.reference_json = json.load(open(resolve_path_from_project_dir('configs/reference.json')))
        self.entity_config = json.load(open(resolve_path_from_project_dir('configs/entity_configuration.json')))

    def tag_words(self):
        for each_sentence in self.input.split("."):
            self.tag_sentence(each_sentence)

    def tag_sentence(self, each_sentence):
        for counter in range(len(self.priority_configs)):
            for each_tag_strategy in self.rules_config:
                if each_tag_strategy['pattern_type'] == self.priority_configs[counter]:
                    self.process_strategy(each_tag_strategy, each_sentence)

    def process_strategy(self, each_tag_strategy, each_sentence):
        print(each_tag_strategy)
        print(each_sentence)


if __name__ == '__main__':
    auto_tag_processor = AutoTagProcessor(resolve_path_from_project_dir('configs/input_data.txt'))
    auto_tag_processor.tag_words()
