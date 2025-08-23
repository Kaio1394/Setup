from app.utils.files_and_folder_utils import FilerAndFolderUtils
import tkinter as tk
from tkinter import messagebox

if '__main__' == __name__:
    """
    Creating RPA, Logs, Input and Output Folders
    """
    if not FilerAndFolderUtils.directory_rpa_exists():
        FilerAndFolderUtils.create_dir_rpa()
        
    if not FilerAndFolderUtils.file_config_json_exists():
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Configuration error", "The file config.json not found!")
        exit(1)
