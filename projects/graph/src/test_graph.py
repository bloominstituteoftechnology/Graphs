import unittest
from graph import Vertex


class VertexTests(unittest.TestCase):
    def tearDown(self):
        Vertex.all_vertices = set()

    def test_constructor(self):
        v0 = Vertex('V0')

        """
        Raise exception if there is an attempt to create vertices with
        duplicate labels
        """
        vertex = 'V0'
        self.assertRaises(Exception, Vertex, vertex)

        """
        Raise exception if there is an attempt to create a vertex with an edge
        that does not exist
        """
        vertex = 'V4'
        edges = ['V5']
        self.assertRaises(Exception, Vertex, vertex, edges)

    def test_add_edge(self):
        v0 = Vertex('V0')
        v1 = Vertex('V1')
        v10 = ''

        """
        Add edge to vertex
        """
        v0.add_edge(v1)
        self.assertTrue(v1 in v0.edges)

        """
        Raise exception if there is an attempt to create an edge with
        nonexistent vertex
        """
        self.assertRaises(Exception, v0.add_edge, v10)

        """
        Raise an exception is there is an attempt to create duplicate edges
        """
        self.assertRaises(Exception, v0.add_edge, v1)


if __name__ == '__main__':
    unittest.main()
