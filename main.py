# Main file for running script
#from src.astar import *
from src.node import *
from src.Map import Map_Obj



def main():
    print("Zyzz legacy")
    new_Map = Map_Obj()

    path = [[0,0], [4,8], [13,2]]
    #path = astar(new_Map.get_start_pos(), new_Map.get_end_goal_pos())

    for x in path:
        new_Map.set_cell_value(x, '.')

    new_Map.show_map()


if __name__ == '__main__':
    main()
