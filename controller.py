from model import Model
from view import View
from APIs.google_APIs_controller import Google_APIs_Controller


class Controller():
    def __init__(self, model:Model, view:View) -> None:
        self.model = model
        self.view = view
        self.google_APIs_controller = Google_APIs_Controller()

    def search(self):
        places = self.google_APIs_controller.places_search(query="OK..")
        print(places)
        
    def run(self):
        self.view.mainloop()