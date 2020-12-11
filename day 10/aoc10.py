import sys

def main():
    with open(sys.argv[1]) as f:
            adapters = sorted([int(l) for l in f])
            adapters = [0] + adapters + [adapters[-1] + 3]
            diffs = [b - a for a, b in zip(adapters, adapters[1:])]
            
            p1 = sum(d == 3 for d in diffs) * sum(d == 1 for d in diffs)

            arranges = {0: 1}
            for a in adapters[1:]:
                arranges[a] = arranges.get(a - 1, 0) + arranges.get(a - 2, 0) + arranges.get(a - 3, 0)

            p2 = arranges[adapters[-1]]


    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
