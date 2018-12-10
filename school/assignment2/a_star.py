import queue as Queue
from game_controller import GameController
from copy import deepcopy


class AStar:

    def perform(puzzle, row, col):
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

        ret = []
        for i in range(row):
            for e in range(col):
                if coord.count((str(i) + str(
                        e))) % 2 == 1:  # if coordinates occur in any muitple of two then it is the same as not performing the move so we only want odd number moves
                    listofmoves.append(str(i) + str(e))
                    ret.append([str(i), str(e)])

        return ret





    def perform2(puzzle, row, col):
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
                                    deepcopy(pmove),
                                    deepcopy(coord))))  # Keep track of the path that leads to the state
                                coord.pop()


                            elif (lights == 5):  # prioritize puzzles that have one more move to solve next
                                moves[deepcopy(check)] = "visited"
                                q.put((2, state))  # put the state in our queue
                                coord.append(c)
                                path.put((2, (
                                    deepcopy(pmove),
                                    deepcopy(coord))))  # Keep track of the path that leads to the state
                                coord.pop()


                            elif (lights == 3):  # prioritize puzzles that have one more move to solve next
                                moves[deepcopy(check)] = "visited"
                                q.put((3, state))  # put the state in our queue
                                coord.append(c)
                                path.put((3, (
                                    deepcopy(pmove),
                                    deepcopy(coord))))  # Keep track of the path that leads to the state
                                coord.pop()

                            else:  # else treat as a regular state to explore
                                moves[deepcopy(check)] = "visited"
                                q.put((4, state))  # put the state in our queue
                                coord.append(c)
                                path.put((4, (
                                    deepcopy(pmove),
                                    deepcopy(coord))))  # Keep track of the path that leads to the state
                                coord.pop()

            junk, fifo = q.get()  # get the highest priority state
            priority, info = path.get()
            coord = info[1]

        ret = []
        for i in range(row):
            for e in range(col):
                if coord.count((str(i) + str(
                        e))) % 2 == 1:  # if coordinates occur in any muitple of two then it is the same as not
                    # performing the move so we only want odd number moves
                    listofmoves.append(str(i) + str(e))
                    ret.append([str(i), str(e)])

        return ret
