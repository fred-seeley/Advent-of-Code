import re, sys
from collections import Counter

dirs = {'e': 2, 'se': 1-1j, 'sw': -1-1j, 'w': -2, 'nw': -1+1j, 'ne': 1+1j}

def neighbours(t):
    return [t + d for d in dirs.values()]

def main():
    with open(sys.argv[1]) as f:
        tiles = [re.findall(r'e|se|sw|w|nw|ne', l) for l in f]
        tiles = [sum(dirs[d] for d in t) for t in tiles]

        black_tiles = {t for t, c in Counter(tiles).items() if c % 2}
        p1 = len(black_tiles)

        for _ in range(100):
            possible_tiles = Counter(n for t in black_tiles for n in neighbours(t))
            black_tiles = [t for t, c in possible_tiles.items() if (t in black_tiles and c == 1) or c == 2]

        p2 = len(black_tiles)

    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
