from game import game
from menu import menu

if __name__ == '__main__':
    model=int(menu())
    # print(type(model))
    # print(model)

    board=[[None,None,None],
           [None,None,None],
           [None,None,None]]
    game(model,board)

