import random  # randint()


class GameController:

    def create_puzzle(rows, cols):
        print("Welcome to the Lights Out Game!")
        puzzle = []
        for i in range(rows):
            puzzle.append([])
            for y in range(cols):
                puzzle[i].append(' 0 ')
        return puzzle




    # Perform_Move function
    # Toggles the lights on or off depending on what you decide to click
    # toggels the four surronding lights (top, bottom, right, left) as well
    def perform_move(puzzle, row, col):
        totalc = len(puzzle[1])  # total number of columns
        totalr = len(puzzle)  # total number of rows

        if puzzle[row][col] == " 1 ":  # if the coordinate we select is "on"
            puzzle[row][col] = " 0 "  # turn light off
        elif puzzle[row][col] == " 0 ":  # if the coordinate we select is "off
            puzzle[row][col] = " 1 "  # turn the light on
        if row > 0:
            if puzzle[row - 1][col] == " 0 ":  # turn top light on
                puzzle[row - 1][col] = " 1 "
            elif puzzle[row - 1][col] == " 1 ":
                puzzle[row - 1][col] = " 0 "  # turn top light off
        if row < (totalr - 1):
            if puzzle[row + 1][col] == " 0 ":  # turn bottom light on
                puzzle[row + 1][col] = " 1 "
            elif puzzle[row + 1][col] == " 1 ":
                puzzle[row + 1][col] = " 0 "  # turn bottom light off
        if col < (totalc - 1):
            if puzzle[row][col + 1] == " 0 ":  # tun right light on
                puzzle[row][col + 1] = " 1 "
            elif puzzle[row][col + 1] == " 1 ":
                puzzle[row][col + 1] = " 0 "  # turn right light off
        if col > 0:
            if puzzle[row][col - 1] == " 0 ":  # turn left light on
                puzzle[row][col - 1] = " 1 "
            elif puzzle[row][col - 1] == " 1 ":
                puzzle[row][col - 1] = " 0 "  # turn left light off
        return puzzle




    # scramble function, goes through grid and turns on every light based on a 50%
    # chance
    def scramble(puzzle):
        totalc = len(puzzle[1])  # find out the number of colums
        totalr = len(puzzle)  # find out the number of rows
        for i in range(totalr):
            for e in range(totalc):
                rand = random.randint(0, 1)  # based on a 50% chance
                if rand == 1:  # use perform_move function
                    GameController.perform_move(puzzle, i, e)
        return puzzle  # return "scrambled" puzzle




    # Is solved puzzel checks to see if all the lights on the grid have been turned
    # off. If all the lights are off then the puzzle has been solved
    def is_solved(puzzle):
        totalc = len(puzzle[1])  # number of columms
        totalr = len(puzzle)  # number of rows
        counter = 0
        for i in range(totalr):
            for e in range(totalc):
                if puzzle[i][e] == " 1 ":
                    counter = (counter + 1)  # Keep a counter of how many lights are
                    # still on
        if counter > 0:  # If any lights are still on then keep the game going
            return 0
        if (puzzle == "empty"):  # a check for for visted nodes
            return 0
        else:  # else if the lights are all off then return 1 to terminate the game
            print("congrats the game is solved!")
            print("*****************************")
            print("Goodbye!!")
            return 1




    def count_lights(puzzle):
        totalc = len(puzzle[1])  # number of columns
        totalr = len(puzzle)  # number of rows
        counter = 0
        for i in range(totalr):
            for e in range(totalc):
                if puzzle[i][e] == "[ 1 ]":  # check to see if the square has a light on
                    counter = (counter + 1)
        return counter
