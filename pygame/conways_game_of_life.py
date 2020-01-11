import pygame
from random import randrange
from time import sleep

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

WIDTH = 20
HEIGHT = 20

UNITSIZE = 10

SPEED = 100

cells = []

pygame.init()
screen = pygame.display.set_mode((WIDTH * UNITSIZE, HEIGHT * UNITSIZE))


class Cell(object):
    def __init__(self, _x, _y):
        self.randomize()
        self.x = _x
        self.y = _y
        self.neighbours = [
            (-1, -1),
            (0, -1),
            (1, -1),
            (-1, 0),
            (1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        ]

    def randomize(self):
        self.state = randrange(0, 2)

    def check_neighbours(self):
        count = 0
        for x_offset, y_offset in self.neighbours:
            if (
                self.x + x_offset >= 0
                and self.x + x_offset <= WIDTH - 1
                and self.y + y_offset >= 0
                and self.y + y_offset <= HEIGHT - 1
            ):
                if cells[self.x + x_offset][self.y + y_offset].state == 1:
                    count += 1
        return count

    def flip(self):
        if self.state == 1:
            self.state = 0
        else:
            self.state = 1

    def update(self):
        count = self.check_neighbours()
        if self.state == 1 and (count == 2 or count == 3):
            pass
        elif self.state == 0 and count == 3:
            self.state = 1
        else:
            self.state = 0


def update():
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if cells[x][y].state == 1:
                color = WHITE
            elif cells[x][y].state == 0:
                color = BLACK
            else:
                color = RED

            cells[x][y].update()

            pygame.draw.rect(
                screen,
                color,
                pygame.Rect(
                    x * UNITSIZE,
                    y * UNITSIZE,
                    (x * UNITSIZE) + UNITSIZE,
                    (y * UNITSIZE) + UNITSIZE,
                ),
            )

    pygame.display.flip()


def generate():
    # generate board #
    # cells = []
    for x in range(WIDTH):
        cells.append([])
        for y in range(HEIGHT):
            cells[x].append(Cell(x, y))


def main():
    done = False
    time = 0
    generate()
    while not done:
        #print("Time: ", time)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                cur_x, cur_y = pygame.mouse.get_pos()
                print ("X: ", int(cur_x/UNITSIZE))
                print ("Y: ", int(cur_y/UNITSIZE))
                cells[int(cur_x/UNITSIZE)][int(cur_y/UNITSIZE)].flip()
        update()
        time += 1
        sleep(SPEED / 1000)


if __name__ == "__main__":
    main()
