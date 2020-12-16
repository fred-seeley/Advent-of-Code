import sys

def main():
    with open(sys.argv[1]) as f:
        ns = {int(x): i for i, x in enumerate(f.readline().split(','))}

        n = 0
        for i in range(len(ns), 29999999):
            if i == 2019:
                p1 = n
            if n in ns:
                next = i - ns[n]
                ns[n] = i
                n = next
            else:
                ns[n] = i
                n = 0
                
        p2 = n

    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
