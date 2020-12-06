import sys

def main():
    with open(sys.argv[1]) as f:
        ids = {int(''.join(['1' if x in 'BR' else '0' for x in bp]), 2) for bp in f.read().split()}

        p1 = max(ids)
        p2 = max({*range(max(ids))} - ids)

    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
