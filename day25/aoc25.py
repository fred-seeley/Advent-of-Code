import functools, sys

def transform(subnum, v):
    return (v * subnum) % 20201227

def main():
    with open(sys.argv[1]) as f:
        cpk, dpk = (int(x) for x in f)

        v, cls = 1, 0
        while (v := transform(7, v)) != cpk:
            cls += 1

        p1 = functools.reduce(transform, [dpk] * cls)

    print(p1)


if __name__ == "__main__":
    main()
