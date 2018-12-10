from copy import deepcopy  # for deepcopy

from game_controller import GameController
from bfs import BFS
from dfs import DFS
from a_star import AStar



row = int(input('Enter number of Rows (Must be > 1): '))
col = int(input('Enter number of Columns (Must be > 1): '))
puzzel = GameController.create_puzzle(row, col)

puzzel = GameController.scramble(puzzel)
puzzelorg = deepcopy(puzzel)
puzzeldfs = deepcopy(puzzel)


for n in puzzel:
    print("".join(n))

# -------------------------------------------------------------------------
# uncomment this block to use the dfs_ai search algorithm
# moves = DFS.perform(puzzel, row, col)

# uncomment to use the A* search
# moves =  AStar.myastar_ai(puzzel, row,col)

# uncomment to use the BFS
moves = BFS.perform(puzzel,row,col)
# -------------------------------------------------------------------------

print("now you try!")
for r in puzzelorg:
    print("".join(r))


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
for move in moves:
    x = int(move[0])
    y = int(move[1])

    puzzelorg = GameController.perform_move(puzzelorg, y, x)
    for n in puzzelorg:
        print("".join(n))

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
