from tkinter import *
from tkinter import ttk
import customtkinter
from settings import *

class View(customtkinter.CTk):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.geometry("1200x800")
        self.title(MAIN_WINDOW_TITLE)
