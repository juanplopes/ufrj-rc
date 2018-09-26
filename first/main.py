from graph_tool.all import *
import numpy

#g = load_graph("power.gml")
# Power grid: An undirected, unweighted network representing the topology of the Western States Power Grid of the United States. Data compiled by D. Watts and S. Strogatz and made available on the web here. Please cite D. J. Watts and S. H. Strogatz, Nature 393, 440-442 (1998).

#g = load_graph("company_edges.xml.gz")
#http://snap.stanford.edu/data/gemsec-Facebook.html

#g = load_graph("email-Eu-core.xml.gz")
#http://snap.stanford.edu/data/email-Eu-core.html

g = load_graph("adjnoun.gml")
#adjacency network of common adjectives and nouns in the novel David Copperfield by Charles Dickens. Please cite M. E. J. Newman, Phys. Rev. E 74, 036104 (2006).

def stats(it):
    it = list(it)
       
    return {
        'min': min(it), 
        'max': max(it), 
        'avg': numpy.average(it), 
        'stdev': numpy.std(it), 
        'count': len(it)
    }
    
def pairs(n, value):
    for i in range(n):
        v = value[i]
        for j in range(i+1, n):
            yield v[j]
    
n = len(list(g.vertices()))

print 'degree'
print '   ', stats(v.out_degree() for v in g.vertices())
print 'clustering'
print '   ', stats(local_clustering(g))
print 'distance'
print '   ', stats(pairs(n, shortest_distance(g)))
print 'components'
print '   ', stats(label_components(g)[1])
print 'pagerank'
print '   ', stats(pagerank(g))
print 'betweeness'
print '   ', stats(betweenness(g)[0])
