from graph_tool.all import *
import numpy, collections

#g = load_graph("power.gml")
# Power grid: An undirected, unweighted network representing the topology of the Western States Power Grid of the United States. Data compiled by D. Watts and S. Strogatz and made available on the web here. Please cite D. J. Watts and S. H. Strogatz, Nature 393, 440-442 (1998).

g = load_graph("company_edges.xml.gz")
#http://snap.stanford.edu/data/gemsec-Facebook.html

#g = load_graph("email-Eu-core.xml.gz")
#http://snap.stanford.edu/data/email-Eu-core.html

#g = load_graph("adjnoun.gml")
#adjacency network of common adjectives and nouns in the novel David Copperfield by Charles Dickens. Please cite M. E. J. Newman, Phys. Rev. E 74, 036104 (2006).


c = collections.Counter(v.out_degree() for v in g.vertices())
for degree, count in sorted(c.items()):
    print degree, '\t', count
