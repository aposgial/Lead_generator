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

    def _add_level(self, window_size:str="650x700", window_title:str="" , frame_width:int=550, frame_height:int=600):
        new_level = customtkinter.CTkToplevel()
        new_level.geometry(window_size)
        new_level.title(window_title)

        new_level.rowconfigure(0 ,weight=1)
        new_level.columnconfigure(0, weight=1)
        return self._add_frame(root=new_level, width=frame_width, height=frame_height)
    
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
        def dinder():
            search_values = self._get_focus_values_table(root=searched_leads_table)
            self.controller.main_window_view_searched_lead_button(search_values[0])

        table_frame = self._add_frame(root=self, width=1078, height=678)
        searched_leads_table = self._add_table(root=table_frame, table_columns=main_table_columns , height=20)

        self._add_table_values(root=searched_leads_table, values=self.controller.get_searches_info())

        button_frame = self._add_frame(root=self, width=1078, height=40)
        button_frame.grid(row=2, columnspan=2, padx=10)

        button_search_leads = customtkinter.CTkButton(master=button_frame, text='Search Leads', command=self.controller.main_window_search_leads_button, width=120, height=32, border_width=0, corner_radius=8)
        button_search_leads.grid(row=1, column=1, padx=10)

        button_view_searched_lead = customtkinter.CTkButton(master=button_frame, text='View Lead', command=dinder, width=120, height=32, border_width=0, corner_radius=8)
        button_view_searched_lead.grid(row=1, column=2, padx=10)

    def search_leads_window(self):
        search_leads_window = self._add_level(window_size="350x200", window_title="Search leads", frame_height=150, frame_width=300)
        search_leads_entry = customtkinter.CTkEntry(master=search_leads_window, width=280, height=30, border_width=2, corner_radius=10)
        search_leads_entry.grid(row=1, column=1)

        #entry_text = search_leads_entry.get()
        #print(entry_text, "ok..")

        button_search_leads_submit = customtkinter.CTkButton(master=search_leads_window, text='Search Leads', command=(
                lambda query = search_leads_entry: self.controller.search_leads_window_submit_button(query)),
                width=120, height=32, border_width=0, corner_radius=8)
        button_search_leads_submit.grid(row=2, column=1, padx=10)

    def leads_window(self, lead_id):
        print(lead_id)
        leads_level = self._add_level(window_size="1200x750", window_title="leads", frame_width=1078, frame_height=678)
        leads_table = self._add_table(root=leads_level, table_columns=main_table_columns , height=20)

        self._add_table_values(root=leads_table, values=self.controller.get_places_info(lead_id))

        #button_frame = self._add_frame(root=self, width=1078, height=40)
        #button_frame.grid(row=2, columnspan=2, padx=10)

        #button_search_leads = customtkinter.CTkButton(master=button_frame, text='Search Leads', command=self.controller.main_window_search_leads_button, width=120, height=32, border_width=0, corner_radius=8)
        #button_search_leads.grid(row=1, column=1, padx=10)

        #button_view_searched_lead = customtkinter.CTkButton(master=button_frame, text='View Lead', command=self.controller.main_window_view_searched_lead_button, width=120, height=32, border_width=0, corner_radius=8)
        #button_view_searched_lead.grid(row=1, column=2, padx=10)