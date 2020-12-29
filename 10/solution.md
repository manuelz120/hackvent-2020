# HV20.10 Be patient with the adjacent

For this challenge, we get a binary [DIMACS](https://www.maplesoft.com/support/help/Maple/view.aspx?path=Formats%2FDIMACS) graph file. Moreover, the challenge hints state that we need to convert the file using `binasc` and take a look at the [cliques](https://www.maplesoft.com/support/help/Maple/view.aspx?path=Formats%2FDIMACS) in the graph.

The `binasc` tool mentioned in the challenge description can be used to convert files from the binary `DIMACS` format to a human-readable ASCII version. After searching for a while and trying various implementations of `bin2asc`, I decided to stick with the one found [here](https://imada.sdu.dk/~marco/Teaching/AY2013-2014/DM811/Resources/). As already announced in the challenge description, the program was segfaulting when trying to convert our graph file. A quick debug section showed that the program was crashing because the graph in our input file is bigger than the default buffer size. After increasing the buffer size and making sure the values get stored on the heap and not on the stack, I was able to successfully convert the input file (see [ASCII-Version](./decoded.txt)).

Another thing I noticed during this step was the preamble of the `DIMACS` file. It contains the following comment:

```
c --------------------------------
c Reminder for Santa:
c   104 118 55 51 123 110 111 116 95 84 72 69 126 70 76 65 71 33 61 40 124 115 48 60 62 83 79 42 82 121 125 45 98 114 101 97 100 are the nicest kids.
c   - bread.
c --------------------------------
```

When we decode the sequence of integer values, we get a fake flag (`hv73{not_THE~FLAG!=(|s0<>SO*Ry}-bread`). However, this seems like it could be useful later on. As a next step, I tried to parse the ASCII representation of the graph in Python and find the biggest clique. Unfortunately, this does not give me the correct output. After playing around for a little bit more, I tried searching for a clique that contains the "nice" values from the challenge preamble. This clique exists, and the neighbours of each of the "nice" values finally form our flag:

```python
#!/usr/bin/python3

from networkx import Graph, node_clique_number

edges = []

with open('./decoded.txt', 'r') as input_file:
    edges = list(filter(lambda line: line.startswith("e"), input_file.readlines()))

G = Graph()

for edge in edges:
    _, a, b = edge.strip().split(" ")
    G.add_edge(int(a), int(b))

print(f"Done! Built graph {G.number_of_nodes()}")
print(f"Edge list: {len(G.edges)}")

nice_kids = [104, 118, 55, 51, 123, 110, 111, 116, 95, 84, 72, 69, 126, 70, 76, 65, 71, 33,
 61, 40, 124, 115, 48, 60, 62, 83, 79, 42, 82, 121, 125, 45, 98, 114, 101, 97, 100]

clique_containing_nice_kids = node_clique_number(G, nice_kids)

flag_parts = map(chr, clique_containing_nice_kids.values())
flag = "".join(flag_parts)

print(flag)
```

**Flag:** HV20{Max1mal_Cl1qu3_Enum3r@t10n_Fun!}
