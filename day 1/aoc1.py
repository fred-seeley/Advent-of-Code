import sys
from itertools import combinations
from math import prod

def main():
    with open(sys.argv[1]) as f:

        entries = [int(x) for x in f]

        for e in combinations(entries, 2):
            if sum(e) == 2020:
                p1 = prod(e)

        for e in combinations(entries, 3):
            if sum(e) == 2020:
                p2 = prod(e)

    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
