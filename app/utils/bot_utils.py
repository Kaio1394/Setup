from app.utils.files_and_folder_utils import FilerAndFolderUtils
from app.constants.cmd import INSTALL

def execution_bot(path_dir_bot: str, dict_input_variables: dict, dict_input_bot: dict, dict_output_bot: dict) -> bool:
    pass

def activate_env(path_dir: str):
    try:
        pass
    except Exception as err:
            raise Exception(str(err))
        
def install_lib(path_dir: str, command: str):
    try:
        activate_env(path_dir)
    except Exception as err:
        raise Exception(str(err))

def read_requiriments(path_bot: str):
    lib_to_install = ""
    path_file_requirements = FilerAndFolderUtils.join_paths(path_bot, 'requirements.txt')
    if not FilerAndFolderUtils.file_exists(path_file_requirements):
        raise NotImplementedError()
    
    list_libs, err = FilerAndFolderUtils.get_list_requirements()
    if err:
        raise Exception(err)
    
    try:
        for lib in list_libs:        
            lib_to_install = lib + ' '   
        cmd = INSTALL
        cmd = cmd.replace('@LIBRARIES@', lib_to_install) 
        install_lib(path_bot, cmd)
    except Exception as err:
        raise Exception(str(err))