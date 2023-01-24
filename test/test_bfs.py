# write tests for bfs
import pytest
import sys; print(sys.path)
import search
import search.graph
from search import graph
import networkx as nx

#copied from HW1
#convert a specific value error to a boolean to be fed into an assert statement
def exception_assertion(test_input, tr_func, expected_exception):

    err_handled = True
    try:
        tr_func(test_input[0], test_input[1])
        err_handled = False
    except ValueError as e:
        if str(e) != expected_exception:
            err_handled = False

    return err_handled

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """

    bfs_correct = ['Steven Altschuler', '32036252', 'Lani Wu', '32042149', '31806696', '30727954', 'Hani Goodarzi', 'Luke Gilbert', 'Michael McManus', '33232663', '33483487', '31626775', '31540829', '32025019', '29700475', 'Charles Chiu', 'Martin Kampmann', 'Neil Risch', 'Nevan Krogan', 'Atul Butte', 'Michael Keiser', '33242416', '32790644', '34272374', '32353859', '30944313', '33765435', '31395880', 'Marina Sirota', '31486345']

    gtest = graph.Graph("data/tiny_network.adjlist")
    bfs = gtest.bfs("Steven Altschuler")

    assert exception_assertion(['', None], graph.Graph("data/empty_network.adjlist").bfs, "graph has no nodes"), "unit test for traversal part 1 failed; did not detect empty input graph"

    absent_node = '0'
    assert exception_assertion([absent_node, None], gtest.bfs, f"starting node {absent_node} not found in graph"), f"unit test for traversal part 2 failed; did not detect nonexistent starting node {absent_node}"

    assert len(bfs_correct) == len(bfs), "unit test for traversal part 3 failed; traversal did not explore entire [accessible] graph"

    assert bfs_correct == bfs, "unit test for traversal part 4 failed; traversal did not explore graph in order"


def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """

    bfs_correct = ['Steven Altschuler', '32036252', 'Lani Wu', '32042149', 'Hani Goodarzi', '33232663', 'Charles Chiu']

    gtest = graph.Graph("data/tiny_network.adjlist")
    bfs = gtest.bfs("Steven Altschuler", "Charles Chiu")

    assert exception_assertion(['', None], graph.Graph("data/empty_network.adjlist").bfs, "graph has no nodes"), "unit test for path-finding part 1 failed; did not detect empty input graph"

    absent_node = '0'
    assert exception_assertion([absent_node, None], gtest.bfs, f"starting node {absent_node} not found in graph"), f"unit test for path-finding part 2.0 failed; did not detect nonexistent starting node {absent_node}"
    assert exception_assertion(["Steven Altschuler", absent_node], gtest.bfs, f"ending node {absent_node} not found in graph"), f"unit test for path-finding part 2.1 failed; did not detect nonexistent ending node {absent_node}"

    #beware that if there are multiple equally short shortest paths and graph.py is updated to find a different one, this will fail
    assert bfs_correct == bfs, "unit test for path-finding part 3 failed; did not correctly identify the shortest path"

    gtest2 = graph.Graph("data/disconnected_network.adjlist")
    bfs2 = gtest2.bfs("Steven Altschuler", "Charles Chiu")

    assert bfs2 == None, "unit test for path-finding part 4 failed; did not recognize unreachable end node"