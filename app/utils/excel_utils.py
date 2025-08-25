import pandas as pd
from app.constants.tabs_name import *
from app.constants.general import KEY_FILE_XLSX
from app.utils.json_utils import JsonUtils
from app.variables.global_variables import *

class ExcelUtils:
    @staticmethod
    def load_xlsx_params_input() -> tuple[dict, str]:
        try:
            df: pd.DataFrame
            json_config, err = JsonUtils.read_config_file()
            if err:
                return [], err
            path_file = json_config[KEY_FILE_XLSX]
            df = pd.read_excel(path_file, TAB_PARAMS_INPUT)
            return df[df.iloc[:, 1].notna()].set_index(df.columns[0])[df.columns[1]].to_dict(), ""
        except Exception as err:
            return {}, str(err)
        
    @staticmethod
    def load_xlsx_params_config() -> tuple[dict, str]:
        try:
            df: pd.DataFrame
            json_config, err = JsonUtils.read_config_file()
            if err:
                return [], err
            path_file = json_config[KEY_FILE_XLSX]
            df = pd.read_excel(path_file, TAB_PARAMS_CONFIG)
            return df[df.iloc[:, 1].notna()].set_index(df.columns[0])[df.columns[1]].to_dict(), ""
        except Exception as err:
            return {}, str(err)  
    
    @staticmethod
    def get_list_execution_from_xlsx() -> tuple[list, str]:       
        try:
            df: pd.DataFrame
            list_bots: list = []
            json_config, err = JsonUtils.read_config_file()
            if err:
                return [], err
            path_file = json_config[KEY_FILE_XLSX]
            df = pd.read_excel(path_file, TAB_EXECUTOR)
            list_bots = df.iloc[:, 0].dropna().tolist()            
            return list_bots, ""
        except Exception as err:
            return list_bots, str(err)