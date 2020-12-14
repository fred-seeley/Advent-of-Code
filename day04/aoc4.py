import re, sys

fields = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hgt': lambda x: (x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193) or (x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76),
    'hcl': lambda x: re.match('^#[a-f\d]{6}$', x),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: re.match('^\d{9}$', x),
}

def main():
    with open(sys.argv[1]) as f:
        pps = [dict(x.split(':') for x in l.split()) for l in f.read().split('\n\n')]

        p1 = sum(all(f in pp for f in fields) for pp in pps)
        p2 = sum(all(f in pp and fields[f](pp.get(f, None)) for f in fields) for pp in pps)

    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
