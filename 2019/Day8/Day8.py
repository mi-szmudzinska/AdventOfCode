import os

WIDTH = 25
HEIGHT = 6
SIZE = WIDTH * HEIGHT

BLACK = 0
WHITE = 1
TRANSPARENT = 2

with open(os.path.dirname(__file__) + "/input.txt") as f:
    line = f.readline().strip()
    pixels_iter = iter(line)

    min_zeros = float("inf")
    part1 = 0

    for _ in range(len(line) // SIZE):
        count = [0] * 3

        for y in range(HEIGHT):
            for x in range(WIDTH):
                pixel = int(next(pixels_iter))
                count[pixel] += 1

        if count[0] < min_zeros:
            min_zeros = count[0]
            part1 = count[1] * count[2]

    print("Part 1:", part1)
