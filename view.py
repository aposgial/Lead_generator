from tkinter import *
from tkinter import ttk
from typing import Any
import customtkinter
from settings import *

main_table_columns = ('location_searched', 'type_searched', 'result_sum', 'date_searched', 'suggestions')

class View(customtkinter.CTk):
    def __init__(self, controller, *args, **kwargs) -> None:
        self.controller = controller
        super().__init__(*args, **kwargs)
        self.geometry("1200x750")
        self.title(MAIN_WINDOW_TITLE)
        self.main_window()


    def _add_frame(self, root, width=1100, height=700):
        new_frame = customtkinter.CTkFrame(master=root, width=width, height=height, corner_radius=10)
        new_frame.grid(padx=10, pady=10)
        new_frame.grid_propagate(flag=False)
        return new_frame
    
    def _add_table(self, root:customtkinter.CTkFrame, height=28, columnspan=2, selectmode=BROWSE, table_columns=()):
        new_table = ttk.Treeview(master=root, columns=table_columns, height=height, selectmode=selectmode)
        new_table.grid(padx=25, pady=25, columnspan=columnspan)
        new_table.grid_propagate(flag=False)

        new_table.column("#0", anchor=W,width=0, stretch=NO)
        for table_column in table_columns:
            new_table.column(table_column, anchor=W)
            new_table.heading(table_column, text=table_column, anchor=W)
        return new_table
    
    def _add_table_values(self, root:ttk.Treeview, values:list):
        for iid,value in enumerate(values):
            root.insert(index=END, parent='', values=value)#, iid=iid

    def _get_focus_values_table(self, root:ttk.Treeview):
        return root.item(root.focus()).get("values")
    

    def main_window(self):
        table_frame = self._add_frame(root=self, width=1078,height=678)
        table = self._add_table(root=table_frame, table_columns=main_table_columns , height=20)

        self._add_table_values(root=table, values=self.controller.get_searches_values())