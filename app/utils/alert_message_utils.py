import tkinter as tk
from tkinter import messagebox

def show_message(msg: str):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Configuration error", msg)
    exit(1)