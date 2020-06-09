def get_text_from_file(input_file):
    with open(input_file, 'r') as f:
        text_content = f.read()
        f.close()
    return text_content
