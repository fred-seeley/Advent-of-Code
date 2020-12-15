import sys

def masker(mask, value):
    return (value | int(mask.replace('X', '0'), 2)) & int(mask.replace('X', '1'), 2)

def main():
    with open(sys.argv[1]) as f:
        mem = {}
        for l in f:
            action, value = l.strip().split(' = ')
            if action == 'mask':
                mask = value
            else:
                address = int(action[4:-1])
                mem[address] = masker(mask, int(value))

        p1 = sum(mem.values())

    print(p1)


if __name__ == "__main__":
    main()
