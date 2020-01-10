from os import system
from time import sleep
from colorama import Fore

size = 8
board = [[0 for x in range(size)] for y in range(size)]

moves = [(2, 1), (1, 2), (2, -1), (-1, 2), (-2, 1), (1, -2), (-2, -1), (-1, -2)]

speed = 50

highest_pos = 0
backtrack_pos = 0


def main():
    solve(board, 0, 0, 1)


def solve(_board, cur_x, cur_y, _pos):
    global highest_pos, backtrack_pos
    if isAllowed(_board, cur_x, cur_y):
        if _pos > highest_pos:
            highest_pos = _pos
        show(_board, cur_x, cur_y, _pos)
        _board[cur_x][cur_y] = _pos
        if isCompleted(_board):
            return True
        for x, y in moves:
            if solve(_board, cur_x + x, cur_y + y, _pos + 1):
                return True
        _board[cur_x][cur_y] = 0
        backtrack_pos = _pos
    return False


def isCompleted(_board):
    for x in range(size):
        for y in range(size):
            if _board[x][y] == 0:
                return False
    print("Solution Found:")
    show(_board)
    return True


def isAllowed(_board, _x, _y):
    if _x >= 0 and _x < size and _y >= 0 and _y < size and _board[_x][_y] == 0:
        return True
    return False


def show(_board, _x=0, _y=0, _pos=0):
    system("clear")
    print(
        "Pos: ",
        _pos,
        " | x: ",
        _x,
        " | y: ",
        _y,
        " | max: ",
        highest_pos,
        " | backtrack: ",
        backtrack_pos,
    )
    for row in _board:
        for item in row:
            if item == 0:
                print(Fore.BLACK + str(item).zfill(2) + " " + Fore.RESET, end="")
            else:
                print(str(item).zfill(2) + " ", end="")
        print()
    sleep(speed / 1000)


if __name__ == "__main__":
    main()
