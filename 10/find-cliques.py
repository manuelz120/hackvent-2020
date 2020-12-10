#!/usr/bin/python3

import networkx as nx

edges = []

with open('./decoded.txt', 'r') as input_file:
    edges = list(filter(lambda line: line.startswith("e"), input_file.readlines()))

G = nx.Graph()

for edge in edges:
    _, a, b = edge.strip().split(" ")
    G.add_edge(int(a), int(b))

print(f"Done! Built graph {G.number_of_nodes()}")
print(f"Edge list: {len(G.edges)}")

nice_kids = [104, 118, 55, 51, 123, 110, 111, 116, 95, 84, 72, 69, 126, 70, 76, 65, 71, 33,
 61, 40, 124, 115, 48, 60, 62, 83, 79, 42, 82, 121, 125, 45, 98, 114, 101, 97, 100]

clique_containing_nice_kids = nx.node_clique_number(G, nice_kids)

flag_parts = map(chr, clique_containing_nice_kids.values())
flag = "".join(flag_parts)

print(flag)
# HV20{Max1mal_Cl1qu3_Enum3r@t10n_Fun!}