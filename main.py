# Main file for running script
#from src.astar import *
from src.node import Node
from src.Map import Map_Obj
from src.astar import astar


def main():
    print("WEELCOME TO ASTAR ASSHOLE")
    while True:
        task = int(input("What task do you want to do? "))
        map_obj = Map_Obj(task)
        path = astar(map_obj.get_start_pos(), map_obj.get_end_goal_pos(), map_obj)
        for pos in path:
            map_obj.set_cell_value(pos, 'p')
        map_obj.show_map()

if __name__ == '__main__':
    main()
