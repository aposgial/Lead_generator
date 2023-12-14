from model import Model
from view import View
from controller import controller

def main():
    model = Model()
    view = View()
    App = controller(model, view)
    print(model.read_json_file(model.place_file))
    App.run()

if __name__ == '__main__':
    main()
    