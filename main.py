from model import Model
from view import View
from controller import controller
import sys

def main():
    #print(sys.getrecursionlimit())
    sys.setrecursionlimit(1500)

    model = Model()
    view = View()
    App = controller(model, view)
    App.run()

if __name__ == '__main__':
    main()
    