import os 
from app.constants.path import *
from app.variables.global_variables import base_dir

class FilerAndFolderUtils:
    @staticmethod
    def join_paths(path1: str, path2: str) -> str:
        return os.path.join(path1, path2)
    
    @staticmethod
    def file_exists(path: str) -> bool:
        return os.path.isfile(path)
    
    @staticmethod
    def directory_rpa_exists() -> bool:
        return os.path.isdir(PATH_FOLDER_RPA)
    
    @staticmethod
    def create_dir_rpa():
        os.mkdir(PATH_FOLDER_RPA)
        
    @staticmethod
    def file_config_json_exists() -> bool:
        return os.path.isfile(f"{base_dir}/{PATH_FILE_CONFIG}")
    
    @staticmethod
    def create_directory(path: str):
        try:
            os.mkdir(path)
        except Exception as err:
            return
    
    @staticmethod
    def directory_exists(path: str) -> bool:
        return os.path.isdir(path)
    
    @staticmethod
    def get_list_requirements(path: str) -> tuple[list, str]:
        try:
            with open(path, 'r', encoding='utf=8') as file:
                rows = file.readline()
            list_rows = [row.strip() for row in rows]
            return list_rows, ""
        except Exception as err:
            return [], str(err)