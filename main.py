from app.utils.files_and_folder_utils import FilerAndFolderUtils
from app.utils.excel_utils import ExcelUtils
from app.utils.alert_message_utils import show_message

if '__main__' == __name__:
    """
    Creating RPA, Logs, Input and Output Folders
    """
    if not FilerAndFolderUtils.directory_rpa_exists():
        FilerAndFolderUtils.create_dir_rpa()
        
    if not FilerAndFolderUtils.file_config_json_exists():
        show_message("The file config.json not found!")
    list_execution_bots, err = ExcelUtils.get_list_execution_from_xlsx()
    if err:
        show_message(err)
    for bot in list_execution_bots:
        print(bot)