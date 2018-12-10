import queue as Queue
from game_controller import GameController
from copy import deepcopy


class DFS:

    # depth limited first search Implementation to solve puzzle
    def perform(puzzle, row, col):
        # dictionary to keep track of visited nodes
        moves = {}
        moves[str(deepcopy(puzzle))] = "visited"
        listofmoves = []
        q = Queue.LifoQueue()
        state = puzzle
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
                        pass


                    else:
                        moves[deepcopy(check)] = "visited"  # add state to visited nodes dictionary
                        coord.append(c)
                        q.put(deepcopy(move))  # put the state in our LIFO queue
                        path.append((deepcopy(move), deepcopy(coord)))  # Keep track of the path that leads to the state
                        coord.pop()

            # get the last state added to the queue (LIFO) --> this is the next state to perform move on
            state = q.get()
            currentstate, coord = path.pop()

        ret = []
        for i in range(row):
            for e in range(col):
                if coord.count((str(i) + str(
                        e))) % 2 == 1:  # if coordinates occur in any muitple of two then it is the same as not
                    # performing the move so we only want odd number moves
                    listofmoves.append(str(i) + str(e))
                    ret.append([str(i),str(e)])

        return ret
