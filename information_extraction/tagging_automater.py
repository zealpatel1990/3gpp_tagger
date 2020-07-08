from utils.file_utils import get_text_from_file, write_json_to_file, write_text_to_file
from utils.path_finder import resolve_path_from_project_dir
import json
from word_tagger.rules_tagger import RulesTagger
import copy
import os


class AutoTagProcessor:
    def __init__(self, input_file, target_name):
        self.target_name = target_name
        self.input = get_text_from_file(input_file)
        self.rules_config = json.load(open(resolve_path_from_project_dir('configs/rules.json')))
        self.priority_configs = json.load(open(resolve_path_from_project_dir('configs/processing_priority.json')))
        self.reference_json = json.load(open(resolve_path_from_project_dir('configs/reference.json')))
        self.reference_entity_json = self.reference_json['entities'][0]
        self.reference_json['entities'].clear()
        self.entity_config = json.load(open(resolve_path_from_project_dir('configs/entity_configuration.json')))
        self.rules_tagger = RulesTagger(self.priority_configs, self.rules_config)

    def tag_words(self):
        index = 0
        for each_sentence in self.input.split("."):
            self.tag_sentence(each_sentence, index)
            index = 1 + len(each_sentence)
        return self.write_annotation_text()

    def tag_sentence(self, each_sentence, index):
        annotation_list = self.rules_tagger.process_sentence(each_sentence, index)
        self.prepare_annotation_file(annotation_list)

    def prepare_annotation_file(self, annotation_list):
        for each in annotation_list:
            entity = copy.deepcopy(self.reference_entity_json)
            entity['offsets'][0]['start'], entity['offsets'][0]['text'], entity[
                'classId'] = each[0], each[1], each[2]

    def write_annotation_text(self):
        output_text_file = resolve_path_from_project_dir(os.path.join('configs', self.target_name + '.txt'))
        output_ann_file = resolve_path_from_project_dir(os.path.join('configs', self.target_name + '.ann.json'))
        write_json_to_file(self.reference_json, output_ann_file)
        write_text_to_file(self.input, output_text_file)
        return output_text_file, output_ann_file


if __name__ == '__main__':
    auto_tag_processor = AutoTagProcessor(get_text_from_file(resolve_path_from_project_dir('configs/sample.txt')),
                                          '3ggpp')
    auto_tag_processor.tag_words()
