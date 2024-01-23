from Model.model import Model
from view import View
from APIs.google_APIs_controller import Google_APIs_Controller

from APIs.google_API_client import Google_APIs


class Controller():
    def __init__(self) -> None:
        self.model = Model()
        self.view = View(self)
        #self.view.controller = self
        self.google_APIs_controller = Google_APIs_Controller()

    def search(self):
        places = self.google_APIs_controller.places_search(query="OK..")
        google_api = Google_APIs()
        google_api.write_dict_to_json_file(places)


    def get_searches_values(self):
        return self.model.select_searches()
        
    def run(self):
        self.view.mainloop()