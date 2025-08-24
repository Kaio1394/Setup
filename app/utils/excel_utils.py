import pandas as pd
from app.constants.tabs_name import *
from app.constants.general import KEY_FILE_XLSX
from app.utils.json_utils import JsonUtils

class ExcelUtils:
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