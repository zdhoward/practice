from random import randrange
from itertools import permutations
import math

"""
    Requires python 3.8
"""


def main():
    points = generate_points()
    ##display(points)
    path, distance = find_best_path(points)
    print(f"Shortest Path: {path}")
    print(f"Shortest Distance: {distance}")


def generate_points(_num=10, _x=100, _y=100):
    points = []
    for i in range(_num):
        points.append((randrange(0, _x), randrange(0, _y)))
    return points


def find_best_path(_points):
    all_paths = permutations(range(len(_points)))
    shortest_path = None
    shortest_distance = None

    for path in all_paths:
        distance = calculate_path_distance(_points, path)
        if shortest_distance == None:
            shortest_distance = distance
            shortest_path = path
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = path

    taken_path = [_points[item] for item in shortest_path]

    return taken_path, shortest_distance


def calculate_path_distance(_points, _path):
    distance = 0
    for i in range(len(_path) - 1):
        distance += math.dist(_points[_path[i]], _points[_path[i + 1]])
    return distance


def display(_points):
    for x, y in _points:
        print(f">> x: {x}, y: {y}")


if __name__ == "__main__":
    main()
