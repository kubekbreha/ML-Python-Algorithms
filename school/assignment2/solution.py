import random  # randint()
import queue as Queue  # for BFS/DFS/A*
from copy import deepcopy  # for deepcopy
import math  # operations
import time  # stopwatch


from game_controller import GameController
from bfs import BFS



def myastar_ai(puzzle, row, col):
    listofmoves = []
    q = Queue.PriorityQueue()
    state = puzzle
    fifo = puzzle
    steps = 0
    moves = {}
    moves[str(deepcopy(puzzle))] = "visited"
    lights = 0
    path = Queue.PriorityQueue()
    coord = ["start"]

    while (GameController.is_solved(fifo) != 1):

        for i in range(row):
            for e in range(col):

                pmove = GameController.perform_move(deepcopy(fifo), i, e)  # perform move on the puzzel
                check = str(pmove)
                steps = steps + 1  # count the number of steps
                state = deepcopy(pmove)
                lights = GameController.count_lights(pmove)  # count the number of lights
                c = str(e) + str(i)  # store coordinates of move in C

                if check in moves:
                    # if node has been been visited then do nothing
                    a = 0


                else:

                    if (lights == 0):
                        # prioritize puzzles that have been solved
                        moves[deepcopy(check)] = "visited"
                        q.put((1, state))  # put the state in our queue
                        coord.append(c)
                        check2 = deepcopy(coord)
                        path.put((1, (deepcopy(pmove), check2)))  # Keep track of the path that leads to the state
                        coord.pop()


                    elif (lights == 3):  # prioritize puzzles that have one more move to solve next
                        moves[deepcopy(check)] = "visited"
                        q.put((2, state))  # put the state in our queue
                        coord.append(c)
                        check2 = deepcopy(coord)
                        path.put((2, (deepcopy(pmove), check2)))  # Keep track of the path that leads to the state
                        coord.pop()

                    else:  # else treat as a regular state to explore
                        moves[deepcopy(check)] = "visited"
                        q.put((3, state))  # put the state in our queue
                        coord.append(c)
                        check2 = deepcopy(coord)
                        path.put((3, (deepcopy(pmove), check2)))  # Keep track of the path that leads to the state
                        coord.pop()

        junk, fifo = q.get()  # get the highest priority state
        priority, info = path.get()
        coord = info[1]

    for i in range(row):
        for e in range(col):
            if coord.count((str(i) + str(
                    e))) % 2 == 1:  # if coordinates occur in any muitple of two then it is the same as not performing the move so we only want odd number moves
                listofmoves.append(str(i) + str(e))
                print("Make this move: ", str(i) + str(e))

    return len(listofmoves), steps


def dfs_ai(puzzle, row, col):  # depth limited first search Implementation to solve puzzle
    moves = {}  # dictionary to keep track of visited nodes
    moves[str(deepcopy(puzzle))] = "visited"
    listofmoves = []
    q = Queue.LifoQueue()
    state = puzzle
    currentstate = puzzel
    steps = 0
    path = []
    coord = ["start"]
    path.append((state, coord))

    while (GameController.is_solved(state) != 1):  # while puzzle is not solved
        for i in range(row):
            for e in range(col):
                move = GameController.perform_move(deepcopy(state), i, e)  # perform move on puzzle
                check = str(move)
                steps = steps + 1  # count the number of steps
                c = str(e) + str(i)  # store coordinates of move in C
                if check in moves:  # if node has been visited then do nothing
                    a = 0


                else:
                    moves[deepcopy(check)] = "visited"  # add state to visited nodes dictionary
                    coord.append(c)
                    q.put(deepcopy(move))  # put the state in our LIFO queue
                    path.append((deepcopy(move), deepcopy(coord)))  # Keep track of the path that leads to the state
                    coord.pop()

        state = q.get()  # get the last state added to the queue (LIFO) --> this is the next state to perform move on
        currentstate, coord = path.pop()

    for i in range(row):
        for e in range(col):
            if coord.count((str(i) + str(
                    e))) % 2 == 1:  # if coordinates occur in any muitple of two then it is the same as not performing the move so we only want odd number moves
                listofmoves.append(str(i) + str(e))
                print("Make this move: ", str(i) + str(e))

    return len(listofmoves), steps


def bonusastar_ai(puzzle, row, col):
    listofmoves = []
    q = Queue.PriorityQueue()
    state = puzzle
    fifo = puzzle
    steps = 0
    moves = {}
    moves[str(deepcopy(puzzle))] = "visited"
    lights = 0
    path = Queue.PriorityQueue()
    coord = ["start"]

    while (GameController.is_solved(fifo) != 1):

        for i in range(row):
            for e in range(col):

                if (fifo != "empty"):  # empty is used to represent nodes that have been visited

                    pmove = GameController.perform_move(deepcopy(fifo), i, e)  # perform move on the puzzel
                    check = str(pmove)
                    steps = steps + 1  # count the number of steps
                    state = deepcopy(pmove)
                    lights = GameController.count_lights(pmove)  # count the number of lights
                    c = str(e) + str(i)  # store coordinates of move in C

                    if check in moves:  # if node has been been visited then do nothing
                        a = 0


                    else:
                        if (lights == 0):  # prioritize puzzles that have been solved
                            moves[deepcopy(check)] = "visited"
                            q.put((1, state))  # put the state in our queue
                            coord.append(c)
                            path.put((1, (
                            deepcopy(pmove), deepcopy(coord))))  # Keep track of the path that leads to the state
                            coord.pop()


                        elif (lights == 5):  # prioritize puzzles that have one more move to solve next
                            moves[deepcopy(check)] = "visited"
                            q.put((2, state))  # put the state in our queue
                            coord.append(c)
                            path.put((2, (
                            deepcopy(pmove), deepcopy(coord))))  # Keep track of the path that leads to the state
                            coord.pop()


                        elif (lights == 3):  # prioritize puzzles that have one more move to solve next
                            moves[deepcopy(check)] = "visited"
                            q.put((3, state))  # put the state in our queue
                            coord.append(c)
                            path.put((3, (
                            deepcopy(pmove), deepcopy(coord))))  # Keep track of the path that leads to the state
                            coord.pop()

                        else:  # else treat as a regular state to explore
                            moves[deepcopy(check)] = "visited"
                            q.put((4, state))  # put the state in our queue
                            coord.append(c)
                            path.put((4, (
                            deepcopy(pmove), deepcopy(coord))))  # Keep track of the path that leads to the state
                            coord.pop()

        junk, fifo = q.get()  # get the highest priority state
        priority, info = path.get()
        coord = info[1]

    for i in range(row):
        for e in range(col):
            if coord.count((str(i) + str(
                    e))) % 2 == 1:  # if coordinates occur in any muitple of two then it is the same as not performing the move so we only want odd number moves
                listofmoves.append(str(i) + str(e))
                print("Make this move: ", str(i) + str(e))

    return len(listofmoves), steps


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

    # dfs_ai(puzzel, row, col)

    # uncomment to use the A* search
    myastar_ai(puzzel, row,col)

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
