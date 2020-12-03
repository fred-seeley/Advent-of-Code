import sys
from math import prod

def main():
    with open(sys.argv[1]) as f:
        lines = [l for l in f]
        slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

        trees = []
        for dx, dy in slopes:
            path = [lines[i * dy][(i * dx) % (len(lines[i]) - 1)] for i in range(len(lines) // dy)]
            trees += [path.count('#')]

        p1 = trees[1]
        p2 = prod(trees)

    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
