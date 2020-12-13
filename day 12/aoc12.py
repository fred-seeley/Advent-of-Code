import math, sys
from collections import namedtuple

Instruction = namedtuple('Instruction', 'action value')

compass = {'E': 1, 'N': 1j, 'W': -1, 'S': -1j}
turn    = {'L': 1, 'R': -1}

def nav(ins, dir=1, waypoint=False):
    pos = 0
    for i in ins:
        if i.action in 'NSEW':
            if waypoint:
                dir += compass[i.action] * i.value
            else:
                pos += compass[i.action] * i.value
        elif i.action in 'LR':
            phi = turn[i.action] * math.radians(i.value)
            dir *= complex(math.cos(phi), math.sin(phi))
        elif i.action == 'F':
            pos += dir * i.value

    return round(abs(pos.real) + abs(pos.imag))

def main():
    with open(sys.argv[1]) as f:
        ins = [Instruction(l[0], int(l[1:])) for l in f]

        p1 = nav(ins)
        p2 = nav(ins, 10 + 1j, True)

    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
