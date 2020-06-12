from utils.config_utils import get_class_from_name


class RulesTagger:

    def process_span_match(self):
        print("process span match")
        start_tag = self.strategy_config['span_match']['start_span_match']
        end_tag = self.strategy_config['span_match']['end_span_match']
        sentence_offset = self.start_index
        return_start_index = -1
        return_end_index = -1
        return_class = get_class_from_name(self.strategy_config['pattern_type'])
        return_text = None
        for char in self.input_sentence:
            sentence_offset = sentence_offset + 1
            if start_tag == char:
                return_start_index = sentence_offset
            elif return_start_index >= 0 and char == end_tag:
                return_end_index = sentence_offset
        if return_end_index > 0 and return_start_index > 0:
            return_text = self.input_sentence[return_start_index - self.start_index:return_end_index - self.start_index]
        return return_start_index, return_text, return_class

    def process_pattern_match(self):
        self.input_sentence = self.input_sentence.lower()
        return_class = get_class_from_name(self.strategy_config['pattern_type'])
        for each in self.strategy_config['dictionary']:
            return_start_index = self.input_sentence.find(each.lower())
            return_text = each
            if return_start_index > 0:
                break
        return return_start_index, return_text, return_class

    def call_strategy(self, strategy_config, input_sentence, start_index):
        self.input_sentence = input_sentence
        self.strategy_config = strategy_config
        self.start_index = start_index

        if self.strategy_config['function'] == 'process_span_match':
            return self.process_span_match()
        elif self.strategy_config['function'] == 'process_pattern_match':
            return self.process_pattern_match()
