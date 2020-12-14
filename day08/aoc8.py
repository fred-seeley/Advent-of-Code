import sys
from collections import namedtuple

Instruction = namedtuple('Instruction', 'op arg')

def gameboy(code):
    ip, acc, seen = 0, 0, set()
    while ip < len(code):
        seen.add(ip)

        instr = code[ip]
        if instr.op == 'acc':
            acc += instr.arg
        elif instr.op == 'jmp':
            ip += instr.arg - 1

        if (ip := ip + 1) in seen:
            return False, acc

    return True, acc

def main():
    with open(sys.argv[1]) as f:
        code = [Instruction(l.split()[0], int(l.split()[1])) for l in f]

        _, p1 = gameboy(code)

        for i, instr in enumerate(code):
            if instr.op == 'nop':
                instr = Instruction('jmp', instr.arg)
            elif instr.op == 'jmp':
                instr = Instruction('nop', instr.arg)

            halt, acc = gameboy(code[:i] + [instr] + code[(i + 1):])
            if halt:
                p2 = acc
                break

    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
