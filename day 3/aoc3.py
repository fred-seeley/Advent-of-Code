import sys
from math import prod

def path(pattern, slope):
    dx, dy = slope
    x, y = 0, 0

    while y < len(pattern):
        yield pattern[y][x % (len(pattern[0]) - 1)]
        x += dx
        y += dy


def main():
    with open(sys.argv[1]) as f:
        lines = [l for l in f]

        p1 = sum(1 for x in path(lines, (3, 1)) if x == '#')

        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        p2 = prod(sum(1 for x in path(lines, s) if x == '#') for s in slopes)

    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
