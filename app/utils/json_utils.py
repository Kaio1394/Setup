import json
from app.constants.errors import CONFIG_FILE_NOT_FOUND
from app.constants.path import PATH_FILE_CONFIG
from app.utils.files_and_folder_utils import FilerAndFolderUtils
from app.variables.global_variables import base_dir

class JsonUtils:
    @staticmethod
    def read_config_file(path_json: str) -> tuple[dict, str]:
        try:
            if not FilerAndFolderUtils.file_exists(path_json):
                return {}, CONFIG_FILE_NOT_FOUND
            full_path = f"{base_dir}/{PATH_FILE_CONFIG}"
            with open(full_path, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            return dados, ""
        except Exception as err:
            return {}, str(err)