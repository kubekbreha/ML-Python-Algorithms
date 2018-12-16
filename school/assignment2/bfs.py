import queue as Queue
from game_controller import GameController
from copy import deepcopy


class BFS:

    def perform(puzzle, row, col):


        listofmoves = []
        q = Queue.Queue()
        fifo = puzzle
        puzzlee = deepcopy(puzzle)
        steps = 0
        moves = {}  # dictionary that holds the visited nodes to refer to
        path = []
        coord = ["start"]  # list of moves
        path.append((puzzlee, coord))  # keep track of the path of each node

        moves[str(deepcopy(puzzle))] = "visited"  # Add the puzzel as a visited node
        while (GameController.is_solved(fifo) != 1):  # while the puzzle is not solved search for solution

            for i in range(row):
                for e in range(col):

                    pmove = GameController.perform_move(deepcopy(fifo), i, e)  # perform move on the puzzle

                    check = str(pmove)  # add state afer performing move to check
                    steps = steps + 1  # count the number of steps
                    c = str(e) + str(i)  # store coordinates of move in C

                    if check in moves:  # if the node has been visited do nothing
                        pass

                    else:
                        moves[deepcopy(check)] = "visited"  # add the new state to dictionary of visited nodes
                        coord.append(c)
                        q.put(deepcopy(pmove))  # put the state in our LIFO queue
                        path.append(
                            (deepcopy(pmove), deepcopy(coord)))  # Keep track of the path that leads to the state

                        coord.pop()

            fifo = q.get()  # get the first state
            currentstate, coord = path.pop(1)  # get the state and the matching path to get to it

        ret = []
        for i in range(row):
            for e in range(col):
                if coord.count((str(i) + str(
                        e))) % 2 == 1:  # if coordinates occur in any muitple of two then it is the same as not
                    # performing the move so we only want odd number moves
                    listofmoves.append(str(i) + str(e))
                    ret.append([str(i),str(e)])

        return ret
