from utils.config_utils import get_class_from_name
import re


class RulesTagger:

    def __init__(self, priority_configs):
        self.priority_configs = priority_configs

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
        if return_text is None or return_text == '':
            return_start_index, return_end_index, return_text = -1, -1, None
        self.return_list.append((return_start_index, return_text, return_class))

    def process_pattern_match(self):
        self.input_sentence = self.input_sentence
        return_class = get_class_from_name(self.strategy_config['pattern_type'])
        for each in self.strategy_config['dictionary']:
            return_start_index = self.input_sentence.find(each.lower())
            return_text = each
            if return_start_index > 0:
                break
        self.return_list.append((return_start_index, return_text, return_class))

    def regex_match(self):
        self.input_sentence = self.input_sentence
        return_class = get_class_from_name(self.strategy_config['pattern_type'])
        for each in self.strategy_config['dictionary']:
            p = re.compile(each)
            for m in p.finditer(self.input_sentence):
                self.return_list.append((m.start(), m.group(), return_class))

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
        for priority in self.priority_configs:
            for each_tag_strategy in self.rules_config:
                if each_tag_strategy['pattern_type'] == priority['key']:
                    self.call_strategy(each_tag_strategy, self.input_sentence, self.start_index)
        return self.return_list
