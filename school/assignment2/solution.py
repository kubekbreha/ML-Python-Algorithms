from copy import deepcopy  # for deepcopy
import math  # operations
import time  # stopwatch

from game_controller import GameController
from bfs import BFS
from dfs import DFS
from a_star import AStar


###########################################################################
# Main Program Starts Here

print("******************************")
print("Welcome to the Lights Out Game")
print("******************************")
# start = raw_input('Type "start" to begin a new game: ')

# This code block starts
start = "start"
if start == "start":
    row = int(input('Enter number of Rows (Must be > 1): '))
    col = int(input('Enter number of Columns (Must be > 1): '))
    puzzel = GameController.create_puzzle(row, col)

    print("******************************")
    print("Now let's turn some lights ON!")
    print("******************************")
    puzzel = GameController.scramble(puzzel)
    puzzelorg = deepcopy(puzzel)
    puzzeldfs = deepcopy(puzzel)

    # uncomment this code block if you do not want to use the command line to start the game
    '''
    puzzel = create_puzzle(3,3)
    row = 3
    col = 3
    puzzel = scramble(puzzel)
    puzzelorg = deepcopy(puzzel)
    '''

    print("*~*~******LIGHTS ON***********")
    for n in puzzel:
        print("".join(n))

    # uncomment this block to use the dfs_ai search algorithm

    # DFS.perform(puzzel, row, col)

    # uncomment to use the A* search
    AStar.myastar_ai(puzzel, row,col)

    # BFS.perform(puzzel,row,col)

    print("now you try!")
    for r in puzzelorg:
        print("".join(r))

    while (GameController.is_solved(puzzelorg) != 1):
        x = input('Enter an X-coordinate: ')
        y = input('Enter a Y-coordinate: ')
        x = int(x)
        y = int(y)

        if (x >= row) or (y >= col):
            print("Input is out of range")
            print("Please try again")
        else:
            puzzelorg = GameController.perform_move(puzzelorg, y, x)
            for n in puzzelorg:
                print("".join(n))
else:
    print("Input was not recognized, Goodbye")
    exit()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")







# uncomment this block and comment everything above (not including functoions) to run each algorithm 100 times and test robustness
# totalpath = 0
# totalstep = []
# start = time.time()
#
# for r in range(100):
#     puzzel = create_puzzle(5, 5)
#     puzzel = scramble(puzzel)
#     #print "lights on"
#     #for n in puzzel:
#      #   print "".join(n)
#     #path, steps = bfs_ai(puzzel, 4, 4)
#     path, steps = myastar_ai(puzzel,5,5)
#     #path, steps = dfs_ai(puzzel, 4, 4)
#     totalpath = totalpath + path
#     totalstep.append(steps)
#     print ("done")
# print ("length of total path", totalpath)
# print ("length of total step", sum(totalstep))
# end = time.time()
# print(end - start)
