#!/usr/bin/env python3
from time import sleep
from os import system

moves = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

speed = 50


def main():
    size = 10
    grid = [[0 for x in range(size)] for y in range(size)]
    grid[0][0] = 1
    show(grid)

    start_x = start_y = 0
    end_x = end_y = size - 1

    # search(grid, start_x, start_y, end_x, end_y)
    a_star_search(grid, start_x, start_y, end_x, end_y)


def search(_grid, _cur_x, _cur_y, _end_x, _end_y):
    for move_x, move_y in moves:
        new_x = _cur_x + move_x
        new_y = _cur_y + move_y
        if isAllowed(_grid, new_x, new_y):
            if isCompleted(_grid):
                return True
            _grid[new_y][new_x] = 1
            if search(_grid, new_x, new_y, _end_x, _end_y):
                return True
    return False


def a_star_search(_grid, _cur_x, _cur_y, _end_x, _end_y):
    analysis_grid = distance_analysis(_grid, _end_x, _end_y)
    best_val = 999999999
    best_pos = (0, 0)
    for move_x, move_y in moves:
        new_x = _cur_x + move_x
        new_y = _cur_y + move_y
        if analysis_grid[new_x][new_y] < best_val:
            best_val = analysis_grid[new_x][new_y]
            best_pos = (new_x, new_y)
    show(analysis_grid)


def distance_analysis(_grid, _end_x, _end_y):
    analysis_grid = _grid
    for x in range(len(_grid[0])):
        for y in range(len(_grid)):
            distance_x = abs(x - _end_x)
            distance_y = abs(y - _end_y)
            distance = distance_x + distance_y
            # print ("X:", x, "Y:", y, "END_X:", _end_x, "END_Y:", _end_y, "DISTANCE:", distance)
            analysis_grid[y][x] = distance
    return analysis_grid


def isAllowed(_grid, _x, _y):
    if (
        _x >= 0
        and _x < len(_grid[0])
        and _y >= 0
        and _y < len(_grid)
        and _grid[_y][_x] == 0
    ):
        show(_grid)
        return True
    return False


def isCompleted(_grid):
    if _grid[-1][-1] == 1:
        return True
    return False


def show(_grid):
    system("clear")
    for row in _grid:
        for cell in row:
            print(str(cell).ljust(2), end=" ")
        print()
    sleep(speed / 1000)


if __name__ == "__main__":
    main()
