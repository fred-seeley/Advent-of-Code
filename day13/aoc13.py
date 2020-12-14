import operator, sys
from functools import reduce

def main():
    with open(sys.argv[1]) as f:
        t = int(f.readline())
        sched = [(-i, int(id)) for i, id in enumerate(f.readline().split(',')) if id != 'x']

        id = min(sched, key=lambda x: x[1] - (t % x[1]))[1]
        p1 = id * (id - (t % id))

        sum = 0
        prod = reduce(operator.mul, [id[1] for id in sched])
        for a_i, n_i in sched:
            p = prod // n_i
            sum += a_i * pow(p, -1, n_i) * p

        p2 = sum % prod

    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
