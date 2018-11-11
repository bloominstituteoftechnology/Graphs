import unittest
from graph import Graph


class GraphTests(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()  # Instantiate your graph
        self.graph.add_vertex('0')
        self.graph.add_vertex('1')
        self.graph.add_vertex('2')
        self.graph.add_vertex('3')

    def test_add_vertex_and_add_edges(self):
        self.assertDictEqual(self.graph.vertices, {
            '0': set(),
            '1': set(),
            '2': set(),
            '3': set(),
        })
        self.graph.add_edge('0', '1')
        self.graph.add_edge('0', '3')
        self.assertDictEqual(self.graph.vertices, {
            '0': {'1','3'},
            '1': {'0'},
            '2': set(),
            '3': {'0'},
        })
    def test_add_directional_edge(self):
        self.graph.add_directional_edge('0', '3')

if __name__ == '__main__':
    unittest.main()