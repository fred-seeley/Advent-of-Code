import re, sys
from collections import namedtuple

Entry = namedtuple('Entry', 'lo hi char password')

def main():
    with open(sys.argv[1]) as f:
        lines = [re.fullmatch(r'(\d+)-(\d+) (.): (.+)', l.strip()).groups() for l in f]
        entries = [Entry(int(lo), int(hi), char, password) for lo, hi, char, password in lines]

        p1 = sum([e.lo <= e.password.count(e.char) <= e.hi for e in entries])
        p2 = sum([(e.password[e.lo - 1] == e.char) ^ (e.password[e.hi - 1] == e.char) for e in entries])

    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
