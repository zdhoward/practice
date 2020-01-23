from multiprocessing import Pool, cpu_count
from tqdm import tqdm
from time import sleep
from random import randrange


def square(x):
    square = x * x
    sleep(randrange(0, 2))
    return square


if __name__ == "__main__":
    tasks = range(100)
    with Pool(cpu_count()) as pool:
        r = list(tqdm(pool.imap(square, tasks), total=len(tasks)))

    print(r)
