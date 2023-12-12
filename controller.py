from model import Model
from view import View

class controller():
    def __init__(self, model:Model, view:View) -> None:
        self.model = model
        self.view = view

    def run(self):
        self.view.mainloop()