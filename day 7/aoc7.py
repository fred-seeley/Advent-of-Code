import networkx as nx, re, sys
from functools import reduce

def req(DG, source):
    return sum(DG[source][succ]['weight'] * req(DG, succ) for succ in DG.successors(source)) + 1

def main():
    with open(sys.argv[1]) as f:
        DG = nx.DiGraph()

        for line in f:
            source, targets = line.split(' bags contain ')
            DG.add_weighted_edges_from([(source, target, int(w)) for w, target in re.findall(r'(\d+) (\w+ \w+)', targets)])

        p1 = len(nx.ancestors(DG, 'shiny gold'))
        p2 = req(DG, 'shiny gold') - 1

    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
