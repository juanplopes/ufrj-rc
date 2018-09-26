#encoding: utf-8
from graph_tool.all import *
import numpy

#g = load_graph("power.gml")
# Power grid: An undirected, unweighted network representing the topology of the Western States Power Grid of the United States. Data compiled by D. Watts and S. Strogatz and made available on the web here. Please cite D. J. Watts and S. H. Strogatz, Nature 393, 440-442 (1998).

#g = load_graph("company_edges.xml.gz")
#http://snap.stanford.edu/data/gemsec-Facebook.html

#g = load_graph("email-Eu-core.xml.gz")
#http://snap.stanford.edu/data/email-Eu-core.html

#g = load_graph("adjnoun.gml")
#adjacency network of common adjectives and nouns in the novel David Copperfield by Charles Dickens. Please cite M. E. J. Newman, Phys. Rev. E 74, 036104 (2006).

graphname = "email-Eu-core.xml.gz"
g = load_graph(graphname)

def stats(it):
    it = list(it)
       
    return {
        'min': round(min(it), 4), 
        'max': round(max(it), 4), 
        'avg': round(numpy.average(it), 4), 
        'stdev': round(numpy.std(it), 4), 
        'count': len(it)
    }
    
def pairs(n, value):
    for i in range(n):
        v = value[i]
        for j in range(i+1, n):
            yield v[j]
    
def fmtline(name, values):
    return "& {0} & {min} & {max} & {avg} & {stdev}".format(name, **values)
    
n = len(list(g.vertices()))
m = len(list(g.edges()))
comps = len(label_components(g)[1])

print 'degree'
DE = stats(v.out_degree() for v in g.vertices())
print '   ', DE

print 'clustering'
CL = stats(local_clustering(g))
print '   ', CL

print 'distance'
DI = stats(filter(lambda x: x<=n, pairs(n, shortest_distance(g))))
print '   ', DI

print 'components'
CO = stats(label_components(g)[1])
print '   ', CO

print 'pagerank'
PR = stats(pagerank(g))
print '   ', PR

print 'betweeness'
BW = stats(betweenness(g)[0])
print '   ', BW

print """
    \multirow{{3}}{{*}}{{ {0} }}
                  {4} \\\\ 
    \cline{{2-6}} {5} \\\\ 
    \cline{{2-6}} {6} \\\\ 
    \cline{{2-6}} {1} vertices {7} \\\\ 
    \cline{{2-6}} {2} arestas {8} \\\\ 
    \cline{{2-6}} {3} componente(s){9} \\\\ 
""".format(graphname,
    n, m, comps,
    fmtline('Graus', DE),
    fmtline('Clusterização', CL),
    fmtline('Distâncias', DI),
    fmtline('Componentes', CO),
    fmtline('PageRank', PR),
    fmtline('Betweenness', BW))
