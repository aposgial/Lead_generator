from Model.model import Model
from view import View
from controller import Controller

def main():
    model = Model()
    view = View()
    App = Controller(model, view)
    App.search()
    App.run()

if __name__ == '__main__':
    main()
    