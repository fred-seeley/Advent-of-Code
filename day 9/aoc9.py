import sys
from itertools import permutations

def main():
    with open(sys.argv[1]) as f:
        ns = [int(l) for l in f]

        for i in range(25, len(ns)):
            if ns[i] not in [x + y for x, y in permutations(ns[(i - 25):i], 2)]:
                p1 = ns[i]
                break

        i, j, s = 0, 0, ns[0]
        while (s != p1):
            if s < p1:
                j += 1
                s += ns[j]
            else:
                s -= ns[i]
                i += 1

        p2 = min(ns[i:j]) + max(ns[i:j])

    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
