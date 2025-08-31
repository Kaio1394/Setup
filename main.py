from app.utils.files_and_folder_utils import FilerAndFolderUtils
from app.utils.excel_utils import ExcelUtils
from app.utils.alert_message_utils import show_message
from app.utils.bot_utils import execution_bot
import argparse
from app.utils.metrics_utils import insert_metric_access
from app.constants.errors import CONFIG_FILE_NOT_FOUND
import getpass
from datetime import datetime
import socket

dir_main = ""
dir_logs = ""
dir_evidence = ""
dir_input = ""
dir_output = ""

Dict_xlsx_params_input = {}
Dict_xlsx_params_config = {}

Dict_bot_input = {}
Dict_bot_output = {}

PATH_FILE_JSON_CONFIG = "C:\\RPA\\config.json"
msg_result: str = ""

err: str

if '__main__' == __name__:    
    try:
        parser = argparse.ArgumentParser(description="Setup RPA")
        parser.add_argument("--file_config", type=str, help="Configuration file JSON")
        
        args = parser.parse_args()

        if not FilerAndFolderUtils.file_exists(PATH_FILE_JSON_CONFIG):
            show_message(CONFIG_FILE_NOT_FOUND)
            msg_result = CONFIG_FILE_NOT_FOUND
            exit(-1)
        
        # Loading input variable by xlsx
        Dict_xlsx_params_input, msg_result = ExcelUtils.load_xlsx_params_input(PATH_FILE_JSON_CONFIG)
        if msg_result:
            show_message(msg_result)
            exit(-1)
            
        Dict_xlsx_params_config, msg_result = ExcelUtils.load_xlsx_params_config(PATH_FILE_JSON_CONFIG)
        if msg_result:
            show_message(msg_result)
            exit(-1)
        
        # Creating RPA, Logs, Input and Output Folders
        proccess_name = Dict_xlsx_params_config['Process Name']
        dir_main = Dict_xlsx_params_config['Folder Main'] + '/' + proccess_name        
        dir_input = dir_main + Dict_xlsx_params_config['Path Input']
        dir_output = dir_main + Dict_xlsx_params_config['Path Output']
        dir_evidence = dir_main + Dict_xlsx_params_config['Path Evidence']
        dir_logs = dir_main + Dict_xlsx_params_config['Path Logs']
    
        list_directories = [dir_main, dir_logs, dir_input, dir_output, dir_evidence]
        
        for dir in list_directories:
            if not FilerAndFolderUtils.directory_exists(dir):
                FilerAndFolderUtils.create_directory(dir)
        
        # List bots to execute
        list_execution_bots, msg_result = ExcelUtils.get_list_execution_from_xlsx()
        if msg_result:
            show_message(err)
            exit(-1)
        
        datetime_init = datetime.now()  
        for bot_path in list_execution_bots:
            success, msg_result = execution_bot(bot_path, Dict_xlsx_params_input, Dict_bot_input, Dict_bot_output)
            if not success:
                break
    except Exception as err:
        show_message(str(err))
        msg_result = str(err)
    finally:
        datetime_end = datetime.now()  
        insert_metric_successfull, error_insert = insert_metric_access(proccess_name, 
                                                                       msg_result, 
                                                                       getpass.getuser(), 
                                                                       socket.gethostname(),
                                                                       datetime_init, 
                                                                       datetime_end)
        if not insert_metric_successfull:
            show_message(f"Error to insert metric to access: {error_insert}")