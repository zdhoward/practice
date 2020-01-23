#!/usr/bin/env python3
from random import shuffle
from os import system
from time import sleep

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

WALL = 1
PATH = 2
UNSET = 0

speed = 50

solved = []

show_progress = True


def main():
    global solved
    height = 10
    width = 20
    maze = [[0 for x in range(width)] for y in range(height)]
    maze[0][0] = PATH
    generate_maze(maze)
    show(solved)


def generate_maze(_maze, _x=0, _y=0):
    global solved
    _moves = moves
    shuffle(_moves)
    for move_x, move_y in moves:
        maze = _maze
        new_x = _x + move_x
        new_y = _y + move_y
        if isAllowed(_maze, new_x, new_y):
            maze[new_y][new_x] = PATH
            if show_progress:
                show(maze)
            if isCompleted(maze):
                solved = maze
                return True
            if generate_maze(maze, new_x, new_y):
                return True
            maze[new_y][new_x] = UNSET
    return False


def show(_maze):
    system("clear")
    print("+" + "-" * 2 * len(_maze[0]) + "+")
    for row in _maze:
        print("|", end="")
        for item in row:
            if item == UNSET:
                item = " "
            print(item, end=" ")
        print("|")
    print("+" + "-" * 2 * len(_maze[0]) + "+")
    sleep(speed / 1000)


def isAllowed(_maze, _x, _y):
    if (
        _x >= 0
        and _x < len(_maze[0])
        and _y >= 0
        and _y < len(_maze)
        and _maze[_y][_x] == UNSET
    ):
        neighbours = 0
        for move_x, move_y in moves:
            if _x + move_x < len(_maze[0]) and _y + move_y < len(_maze):
                if _maze[_y + move_y][_x + move_x] == PATH:
                    neighbours += 1
        if neighbours == 1:
            return True
    return False


def isCompleted(_maze):
    if _maze[-1][-1] == PATH:
        print("COMPLETED")
        return True
    return False


def add_branching_paths(_maze):
    pass


if __name__ == "__main__":
    main()
