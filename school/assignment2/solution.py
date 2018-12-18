from copy import deepcopy  # for deepcopy

from game_controller import GameController
from bfs import BFS
from dfs import DFS
from a_star import AStar


# work with hash map because checking of already existing state


# -------------------------------------------------------------------------

# row = int(input('Enter number of Rows (Must be > 1): '))
row = 2
# col  int(input('Enter number of Columns (Must be > 1): '))
col = 3
puzzel = GameController.create_puzzle(row, col)

puzzel = GameController.scramble(puzzel)

# puzzel = [[' 0 ', ' 0 ', ' 0 '], [' 1 ', ' 0 ', ' 1 ']]

puzzelorg = deepcopy(puzzel)
puzzeldfs = deepcopy(puzzel)

# -------------------------------------------------------------------------
# uncomment this block to use the dfs_ai search algorithm
moves = DFS.perform(puzzel, row, col)

# uncomment to use the A* search
# moves =  AStar.perform(puzzel, row,col)

# uncomment to use the BFS
# moves = BFS.perform(puzzel, row, col)
# -------------------------------------------------------------------------


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

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


if GameController.is_solved(puzzelorg):
    print("hurray")
else:
    if puzzelorg[0][1] == " 1 ":
        print("hurray")
        puzzelorg = GameController.perform_move(puzzelorg, 0, 2)
        for n in puzzelorg:
            print("".join(n))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif puzzelorg[1][1] == " 1 ":
        print("hurray")
        puzzelorg =GameController.perform_move(puzzelorg, 1, 2)
        for n in puzzelorg:
            print("".join(n))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("hurray")
