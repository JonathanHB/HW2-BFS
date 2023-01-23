import networkx as nx
from queue import Queue

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """

        g = self.graph

        #detect invalid inputs
        if len(g.nodes) == 0:
            raise ValueError("graph has no nodes")

        if start not in g.nodes:
            raise ValueError(f"starting node {start} not found in graph")

        if end is not None and end not in g.nodes:
            raise ValueError(f"ending node {end} not found in graph")

        #queue to store the frontier of the breadth first search
        q = Queue(maxsize=0)

        #track nodes visited thus far
        nodes_visited_in_order = [start]
        #used to reconstruct shortest path
        predecessors = {}
        #determine connectivity
        end_reached = False

        q.put(start)

        #this range should be sufficient as each node will be visited only once by the outer loop
        for i in range(len(g.nodes)):
            # pop the oldest node off the stack
            # this must be (one of) the closest node(s)
            qi = str(q.get())

            #add each of the node's unvisited neighbors to the stack and the list of visited nodes
            for j in list(g.adj[qi]):
                if j not in nodes_visited_in_order:
                    q.put(j)
                    #track which node node j was reached from for shortest path reconstruction
                    predecessors[j] = qi
                    nodes_visited_in_order.append(j)

                    #detect if/when the target node is reached and record that the graph is connected
                    if end is not None and j == end:
                        end_reached = True
                        break

        #if there is no target node
        if end is None:
            return nodes_visited_in_order

        #if there is a reachable target node
        elif end_reached:
            #reconstruct the path taken to reach the target, which must be the (a) shortest path
            #because breadth first search always explores the nearest nodes first.
            nodes_on_shortest_path = [end]
            for x in range(len(g.nodes)):
                nodes_on_shortest_path.append(predecessors[nodes_on_shortest_path[-1]])
                if nodes_on_shortest_path[-1] == start:
                    nodes_on_shortest_path.reverse()
                    return nodes_on_shortest_path

        #if there is an unreachable target node
        else:
            return None

gg = Graph("../data/disconnected_network.adjlist")

print(gg.bfs('Steven Altschuler', 'Charles Chiu')) #, 'Charles Chiu'
print("a")

#plotting for debugging purposes

import matplotlib
import matplotlib.pyplot as plt
from networkx import nx_agraph

wholegraph = nx.read_adjlist("../data/disconnected_network.adjlist", create_using=nx.DiGraph, delimiter=";")

nx.draw(wholegraph, with_labels=True, pos = nx.nx_agraph.graphviz_layout(wholegraph))
#plt.show()



