"""
CULC Breakout Rooms:
(5) 4-person room
(9) 6-person room
(1) 7-person room
(1) 8-person room
(1) 9-person room
(2) 10-person room
(3) 12-person room
"""

import random
import networkx as nx
import matplotlib.pylab as plt

def generate_groups():
    #40 groups generated with random group sizes and times
    possible_hours = list(range(1, 25))
    possible_group_sizes = [4, 6, 7, 8, 9, 10, 12]

    with open('readme.txt', 'w') as f:
        for i in possible_hours[::2]:
            group_sizes = random.sample(possible_group_sizes, 3)
            for x in group_sizes:
                f.write(str(i) + " " + str(x) + "\n")

generate_groups()
inputted_group_size = int(input("Enter the size of your study group: "))
inputted_desired_time = int(input("Enter the start time of your reservation (you will have a 2 hour block). Use 24 hour clock: "))

G = nx.DiGraph()
G.add_nodes_from([1, 2, 3, 4])
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)])
for u, v, d in G.edges(data=True):
   d['weight'] = rd.random()
edges, weights = zip(*nx.get_edge_attributes(G, 'weight').items())
nx.draw(G, node_color='b', edge_color=weights, width=2, with_labels=True)

plt.show()


#return options for rooms
#if no options, ask to restart and select new time
