from utils.config_utils import get_class_from_name
import re


class RulesTagger:

    def __init__(self, priority_configs, rules_config):
        self.priority_configs = priority_configs
        self.rules_config = rules_config

    def handle_entity_load(self, entity_tuple, add_start_index=False):
        if entity_tuple[0] < 1:
            return
        elif entity_tuple[1] is None or entity_tuple[1] == '':
            return
        if add_start_index:
            entity_tuple = (entity_tuple[0] + self.start_index, entity_tuple[1], entity_tuple[2])
        self.return_list.append(entity_tuple)

    def process_span_match(self):
        # print("process span match")
        start_tag = self.strategy_config['span_match']['start_span_match']
        end_tag = self.strategy_config['span_match']['end_span_match']
        sentence_offset = self.start_index
        return_start_index, return_end_index, return_text = -1, -1, None
        return_class = get_class_from_name(self.strategy_config['pattern_type'])
        for char in self.input_sentence:
            sentence_offset = sentence_offset + 1
            if start_tag == char:
                return_start_index = sentence_offset - 1
            elif return_start_index >= 0 and char == end_tag:
                return_end_index = sentence_offset
        if return_end_index > 0 and return_start_index > 0:
            return_text = self.input_sentence[return_start_index - self.start_index:return_end_index - self.start_index]
        else:
            return_start_index, return_end_index, return_text = -1, -1, None
        self.handle_entity_load((return_start_index, return_text, return_class))

    def process_pattern_match(self):
        self.input_sentence = self.input_sentence
        return_class = get_class_from_name(self.strategy_config['pattern_type'])
        for each in self.strategy_config['dictionary']:
            return_start_index = self.input_sentence.find(each.lower())
            return_text = each
            if return_start_index > 0:
                break
        self.handle_entity_load((return_start_index, return_text, return_class), add_start_index=True)

    def regex_match(self):
        self.input_sentence = self.input_sentence
        return_class = get_class_from_name(self.strategy_config['pattern_type'])
        for each in self.strategy_config['dictionary']:
            p = re.compile(each)
            for m in p.finditer(self.input_sentence):
                self.handle_entity_load((m.start(), m.group(), return_class), add_start_index=True)

    def call_strategy(self, strategy_config, input_sentence, start_index):
        self.input_sentence = input_sentence
        self.strategy_config = strategy_config
        self.start_index = start_index

        if self.strategy_config['function'] == 'process_span_match':
            return self.process_span_match()
        elif self.strategy_config['function'] == 'process_pattern_match':
            return self.process_pattern_match()
        elif self.strategy_config['function'] == 'regex_expression_match':
            return self.regex_match()

    def process_sentence(self, input_sentence, start_index):
        self.input_sentence = input_sentence
        self.start_index = start_index
        self.return_list = []
        for value in self.priority_configs:
            each_tag_strategy = self.rules_config[value['key']]
            self.call_strategy(each_tag_strategy, self.input_sentence, self.start_index)
        return self.return_list
