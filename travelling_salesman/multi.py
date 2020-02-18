import multiprocessing as mp
from random import randrange
from itertools import permutations
import math
import time

manager = mp.Manager()
ns = manager.Namespace(
    counter=0, permutation_amt=0, shortest_path=None, shortest_distance=None
)

verbose = False


def calculate_path_distance(_path):
    global verbose
    ns.counter += 1
    if verbose:
        base = str(round((ns.counter / ns.permutation_amt) * 100, 2)).split(".")[0]
        percision = str(round((ns.counter / ns.permutation_amt) * 100, 2)).split(".")[1]
        percent = base + "." + percision.zfill(2)
        print(
            f"{percent}% -> {ns.counter}/{ns.permutation_amt} -> {ns.permutation_amt - ns.counter}",
            end="\r",
        )

    distance = 0
    for i in range(len(_path) - 1):
        distance += math.dist(_path[i], _path[i + 1])

    if ns.shortest_distance == None:
        ns.shortest_distance = distance
        ns.shortest_path = _path
    if distance < ns.shortest_distance:
        ns.shortest_distance = distance
        ns.shortest_path = _path


def generate_points(_num=10, _x=100, _y=100):
    points = []
    for i in range(_num):
        points.append((randrange(0, _x), randrange(0, _y)))
    return points


def find_best_path(_points):
    all_permutations = [item for item in permutations(_points)]
    ns.permutation_amt = len(all_permutations)

    pool = mp.Pool(mp.cpu_count() - 1 or 1)
    pool.map(calculate_path_distance, all_permutations)

    return ns.shortest_path, ns.shortest_distance


def dispatcher():
    manager = mp.Manager()
    return_dict = manager.dict()
    jobs = []
    for i in range(200):
        p = mp.Process(target=worker, args=(i, return_dict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()
    print(return_dict.values())


def main():
    points = generate_points(8)
    start_time = time.time()
    path, distance = find_best_path(points)
    end_time = time.time()
    time_taken = end_time - start_time
    print(f"Time Elapsed: {round(time_taken*1000, 2)}ms")
    print(f"{path} @ {str(round(distance, 2))}")


if __name__ == "__main__":
    main()
