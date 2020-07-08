from information_extraction.pre_process_data import pre_process_file
from information_extraction.tagging_automater import AutoTagProcessor
from services.document_service import DocumentService
from services.settings_service import SettingService


def download_settings():
    # download the project settings for comparision
    setting_service = SettingService()
    setting_service.get_project_setting()


if __name__ == '__main__':
    '''
    Pre-process the data with sentence breaking and remove non-printable characters.
    Domain based Lemmatization
    Note: ## based comments are code and has to be removed appropriately with suitable environments. 
    '''
    ## download_settings()
    pre_processed_file = pre_process_file('configs/input_data.txt')
    # Tag the files using the rules set.
    auto_tag_processor = AutoTagProcessor(pre_processed_file, '3ggpp')
    text_file_path, ann_file_path = auto_tag_processor.tag_words()
    # Using REST call to upload the data into Server.
    ## doc_service = DocumentService()
    ## doc_service.push_annotated_verbatim_text(text_file_path, ann_file_path)
