from app.utils.files_and_folder_utils import FilerAndFolderUtils
from app.utils.excel_utils import ExcelUtils
from app.utils.alert_message_utils import show_message
from app.utils.bot_utils import execution_bot

dir_main = ""
dir_logs = ""
dir_evidence = ""
dir_input = ""
dir_output = ""

Dict_xlsx_params_input = {}
Dict_xlsx_params_config = {}

Dict_bot_input = {}
Dict_bot_output = {}

err: str

if '__main__' == __name__:

    if not FilerAndFolderUtils.file_config_json_exists():
        show_message("The file config.json not found!")
    
    # Loading input variable by xlsx
    Dict_xlsx_params_input, err = ExcelUtils.load_xlsx_params_input()
    if err:
        show_message(err)
        
    Dict_xlsx_params_config, err = ExcelUtils.load_xlsx_params_config()
    if err:
        show_message(err)
     
    # Creating RPA, Logs, Input and Output Folders
    dir_main = Dict_xlsx_params_config['Folder Main'] + '/' + Dict_xlsx_params_config['Process Name']  
    dir_input = dir_main + '/' + Dict_xlsx_params_config['Path Input']
    dir_output = dir_main + '/' + Dict_xlsx_params_config['Path Output']
    dir_evidence = dir_main + '/' + Dict_xlsx_params_config['Path Evidence']
    dir_logs = dir_main + '/' + Dict_xlsx_params_config['Path Logs']
  
    list_directories = [dir_main, dir_logs, dir_input, dir_output, dir_evidence]
    
    for dir in list_directories:
        if not FilerAndFolderUtils.directory_exists(dir):
            FilerAndFolderUtils.create_directory(dir)
    
    # List bots to execute
    list_execution_bots, err = ExcelUtils.get_list_execution_from_xlsx()
    if err:
        show_message(err)
        
    for bot in list_execution_bots:
        success = execution_bot(Dict_xlsx_params_input, Dict_bot_input, Dict_bot_output)
        if not success:
            break