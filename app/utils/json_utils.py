import json
from app.constants.errors import CONFIG_FILE_NOT_FOUND
from app.utils.files_and_folder_utils import FilerAndFolderUtils

class JsonUtils:
    @staticmethod
    def read_config_file() -> tuple[dict, str]:
        try:
            if not FilerAndFolderUtils.file_config_json_exists():
                return {}, CONFIG_FILE_NOT_FOUND
            
        except Exception as err:
            return {}, str(err)