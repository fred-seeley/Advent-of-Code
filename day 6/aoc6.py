import sys

def main():
    with open(sys.argv[1]) as f:
        groups = [[set(x) for x in g.split()] for g in f.read().split('\n\n')]

        p1 = sum(len(set.union(*g)) for g in groups)
        p2 = sum(len(set.intersection(*g)) for g in groups)

    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
