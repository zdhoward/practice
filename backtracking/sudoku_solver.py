from math import ceil
from os import system
from time import sleep
from random import shuffle
from time import process_time as time

# easy
board = [
    [0, 8, 0, 0, 7, 2, 0, 0, 1],
    [0, 5, 0, 0, 3, 1, 6, 4, 9],
    [0, 0, 0, 0, 4, 0, 8, 0, 7],
    [0, 0, 8, 0, 5, 0, 4, 0, 0],
    [0, 4, 0, 0, 0, 0, 2, 0, 8],
    [6, 0, 1, 2, 0, 0, 0, 5, 0],
    [9, 2, 0, 7, 6, 3, 0, 8, 0],
    [0, 7, 0, 0, 1, 0, 0, 6, 2],
    [1, 6, 5, 9, 0, 0, 3, 0, 0],
]

# easy
board = [
    [0, 0, 6, 0, 4, 0, 0, 9, 7],
    [0, 4, 0, 7, 3, 0, 0, 1, 0],
    [0, 1, 7, 0, 9, 2, 0, 3, 0],
    [6, 0, 0, 0, 7, 0, 0, 8, 0],
    [1, 0, 5, 0, 6, 0, 9, 0, 3],
    [0, 2, 0, 0, 1, 0, 0, 0, 6],
    [0, 5, 0, 9, 8, 0, 1, 6, 0],
    [0, 9, 0, 0, 5, 6, 0, 7, 0],
    [8, 6, 0, 0, 2, 0, 3, 0, 0],
]

# very hard
board = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0],
]


solved_board = board

speed = 0

show_progress = False


def main():
    start = time() * 1000
    if solve(board):
        print("Solvable")
    else:
        print("Not Solvable")
    end = time() * 1000
    print(int(end - start), "ms elapsed")


def solve(_board):
    """
    Recursively solve each solvable node
    If no solutions are available, revert
    to the previous step.
    """
    global solved_board
    x, y = nextSolvable(_board)
    if x == -1 and y == -1:
        # -1, -1 = no more solvable nodes
        # meaning the entire board is solved
        print("Completed")
        show(solved_board)
        return True
    else:
        # start trying numbers in the next empty node
        for i in my_shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9]):
            if isAllowed(_board, x, y, i):
                _board[x][y] = i
                if show_progress:
                    show(_board)
                if solve(_board):
                    return True
                _board[x][y] = 0
        return False


def isAllowed(_board, _x, _y, _num):
    """
    Check if the x and y are within bounds
    Check that the suggested number is valid
    """
    if (
        _x >= 0
        and _x < 9
        and _y >= 0
        and _y < 9
        and validate_row(_board, _x, _y, _num)
        and validate_column(_board, _x, _y, _num)
        and validate_box(_board, _x, _y, _num)
    ):
        return True
    return False


def nextSolvable(_board):
    """
    Retrieve the next unsolved node on the board
    """
    global solved_board
    for x in range(9):
        for y in range(9):
            if _board[x][y] == 0:
                return x, y
    solved_board = _board
    return -1, -1


def show(_board):
    """
    Cleanly display the board
    """
    system("clear")
    for row in _board:
        print(row)
    sleep(speed / 1000)


## Validation Rules


def validate_row(_board, _x, _y, _num):
    if _num in _board[_x]:
        return False
    return True


def validate_column(_board, _x, _y, _num):
    occurrences = []
    for x in range(9):
        if _num in occurrences:
            return False
        if _board[x][_y] != 0:
            occurrences.append(_board[x][_y])
    return True


def validate_box(_board, _x, _y, _num):
    occurrences = []
    box_x = ceil((_x + 1) / 3)
    box_y = ceil((_y + 1) / 3)

    for x in range(3):
        box_x = ceil((_x + 1) / 3)
        for y in range(3):
            box_y = ceil((_y + 1) / 3)
            if _num in occurrences:
                return False
            if _board[_x][_y] != 0:
                occurrences.append(_board[_x][_y])
    return True


def my_shuffle(list):
    shuffle(list)
    shuffle(list)
    return list


if __name__ == "__main__":
    main()
