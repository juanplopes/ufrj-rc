from graph_tool.all import *
import csv

g = Graph(directed=False)

with open('email-Eu-core.txt') as txt:
    for row in txt:
        row = row.split(' ')
        g.add_edge(int(row[0]), int(row[1]))
        
g.save('email-Eu-core.xml.gz')


