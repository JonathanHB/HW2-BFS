! [BuildStatus] (https://github.com/JonathanHB/HW2-BFS/workflows/HW2-BFS/badge.svg?event=push)
# Assignment 2
Breadth-first search

Breadth first search (BFS) traverses a graph starting from a single node. It reads other nodes in order of their distance (measured by the minimum number of edges necessary to reach them) from the starting node.

The BFS algorithm implemented here takes a starting node as an argument. It can also take an ending node as an optional argument.
If only a starting node is passed as an argument, the BFS returns a list of all nodes in the graph which are reachable from the starting node in ascending order of their distance from the starting node.

If both a starting and an ending node are passed as arguments, the BFS returns a list of the nodes forming the shortest path from the starting to the ending node, ordered from the starting node to the ending node. 
If multiple equally short such paths exist, one is returned arbitrarily. If the ending node is not reachable from the starting node, the method returns None.
Under the hood this works by running BFS until either the end node is reached or the entire (sub)graph reachable from the starting node has been explored without finding it. 
As each node is reached, it is recorded which node it was reached from. When (and if) the end node is reached, the program follows the dictionary of which node each node was reached from 
(each entry being sort of like an edge) backwards to the start node to reconstruct the shortest path.

Beware that in directed graphs, the shortest path is not commutative (i.e. the shortest path from A to B need not also be the shortest path from B to A).

The instructions below are retained for reference

# Assignment Overview
The purpose of this assignment is to get you comfortable working with graph structures and to implement a breadth-first search function to traverse the graph and find the shortest path between nodes.

# Assignment Tasks

## Coding Assessment
In search/graph.py:
* Define the function bfs that takes in a graph, start node, and optional node and:
	* If no end node is provided, returns a list of nodes in order of breadth-first search traversal from the given start node
	* If an end node is provided and a path exists, returns a list of nodes in order of the shortest path to the end node
	* If an end node is provided and a path does not exist, returns None
* Be sure that your code can handle possible edge cases, e.g.:
	* running bfs traversal on an empty graph
	* running bfs traversal on an unconnected graph
	* running bfs from a start node that does not exist in the graph
	* running bfs search for an end node that does not exist in the graph
	* any other edge cases you can think of 

In test/test_bfs.py:
* Write unit tests for breadth-first traversal and breadth-first search 
* You may use the two networks provided in the data folder or create your own for testing
* Test at least 2 possible edge cases (listed above)
* Include a test case that fails and raises an exception


## Software Development Assessment

* Write unit tests (in the test_bfs.py file) for your breadth first search
* Replace these instructions with a brief description of bfs in your forked repo
	
* Automate Testing with a [Github Actions](https://docs.github.com/en/actions)

	See blogposts below on helping set up github actions with pytest:
	
	* [post 1](https://blog.dennisokeeffe.com/blog/2021-08-08-pytest-with-github-actions)
	* [post 2](https://mattsegal.dev/pytest-on-github-actions.html)
	* Add "! [BuildStatus] (https://github.com/ < your-github-username > /HW2-BFS/workflows/HW2-BFS/badge.svg?event=push)" (update link and remove spaces) to the beginning of your readme file
	* Also refer to previous assignment for more in-depth help with GitHub actions

	Ensure that the github actions complete the following:
	* runs pytest

# Getting Started
To get started you will need to fork this repository onto your own github. You will then work on the code base from your own repo and make changes to it in the form of commits. 

# Reference Information
## Test Data
Two networks have been provided in an adjacency list format readable by [networkx](https://networkx.org/), is a commonly used python package for working with graph structures. These networks consist of two types of nodes:
* Faculty nodes 
* Pubmed ID nodes

However, since these are both stored as strings, you can treat them as equivalent nodes when traversing the graph. The first graph ("citation_network.adjlist") has nodes consisting of all BMI faculty members, the top 100 Pubmed papers *cited by* faculty, and the top 100 papers that *cite* faculty publications. Edges are directed and and edge from node A -> B indicates that node A *is cited by* node B. There are 5120 nodes and 9247 edges in this network.

The second network is a subgraph of the first, consisting of only the nodes and edges along the paths between a small subset of faculty. There are 30 nodes and 64 edges.

# Completing the assignment
Make sure to push all your code to github, ensure that your unit tests are correct, and submit a link to your github through the google classroom assignment.

# Grading

## Code (6 points)
* Breadth-first traversal works correctly (3)
* Traces the path from one faculty to another (2)
* Handles edge cases (1)

## Unit tests (3 points)
* Output traversal for mini data set (1)
* Tests for at least two possible edge cases (1)
* Correctly uses exceptions (1)

## Style (1 points)
* Readable code with clear comments and method descriptions
* Updated README with description of your methods

