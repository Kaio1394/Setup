from app.utils.files_and_folder_utils import FilerAndFolderUtils
from app.constants.cmd import INSTALL
from app.utils.cmd_utils import execute_command, activate_env

def execution_bot(path_dir_bot: str, dict_input_variables: dict, dict_input_bot: dict, dict_output_bot: dict) -> bool:
    try:
        pip_install_requiriments(path_dir_bot) 
    except Exception as err:
        raise Exception(str(err))

def pip_install_requiriments(path_bot: str):
    path_file_requirements = FilerAndFolderUtils.join_paths(path_bot, 'requirements.txt')
    if not FilerAndFolderUtils.file_exists(path_file_requirements):
        raise NotImplementedError()    
    try:
        cmd_script = INSTALL
        cmd_script = cmd_script.replace('@REQUIREMENTS_TXT@', path_file_requirements) 
        activate_env(path_bot)
        execute_command(cmd_script)
    except Exception as err:
        raise Exception(str(err))