import os 
from app.constants.path import *
from app.variables.global_variables import base_dir

class FilerAndFolderUtils:
    @staticmethod
    def directory_rpa_exists() -> bool:
        return os.path.isdir(PATH_FOLDER_RPA)
    
    @staticmethod
    def create_dir_rpa():
        os.mkdir(PATH_FOLDER_RPA)
        
    @staticmethod
    def file_config_json_exists() -> bool:
        return os.path.isfile(f"{base_dir}/{PATH_FILE_CONFIG}")
        