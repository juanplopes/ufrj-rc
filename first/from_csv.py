from graph_tool.all import *
import csv

g = Graph(directed=False)

with open('company_edges.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        g.add_edge(int(row[0]), int(row[1]))
        
g.save('company_edges.xml.gz')


