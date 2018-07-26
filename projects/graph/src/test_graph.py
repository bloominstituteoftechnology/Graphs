import unittest
from graph import Vertex, Graph


class VertexTests(unittest.TestCase):
    def setUp(self):
        Vertex.all_vertices = set()
        Vertex.all_vertix_labels = set()

    def tearDown(self):
        Vertex.all_vertices = set()
        Vertex.all_vertix_labels = set()

    def test_constructor(self):
        """
        Raise exception if there is an attempt to create vertices with
        duplicate labels
        """
        Vertex('V0')
        self.assertRaises(Exception, Vertex, 'V0')


class GraphTests(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def tearDown(self):
        Vertex.all_vertices = set()
        Vertex.all_vertix_labels = set()

    def test_add_vertex(self):
        self.graph.add_vertex('V0')
        self.graph.add_vertex('V1', ['V0'])
        v0 = Vertex._get_obj_instance('V0')

        """
        Should create a Vertex instance
        """
        self.assertTrue('V0' in Vertex.all_vertix_labels)
        self.assertTrue('V1' in Vertex.all_vertix_labels)

        """
        Should add vertex as a vertices key in Graph instance
        """
        self.assertTrue('V0' in self.graph.vertices.keys())
        self.assertTrue('V1' in self.graph.vertices.keys())

        """
        Provided edges should be added to vertices
        """
        self.assertTrue(v0 in self.graph.vertices['V1'])

    def test_add_edge(self):
        self.graph.add_vertex('V0')
        self.graph.add_vertex('V1')
        v0 = Vertex._get_obj_instance('V0')
        v1 = Vertex._get_obj_instance('V1')

        """
        Raise exception when attempting to add an edge that does not exist in
        graph
        """
        self.assertRaises(Exception, self.graph.add_edge, 'V0', 'V2')

        """
        Should add an edge to start vertex
        """
        self.graph.add_edge('V0', 'V1')
        self.assertTrue(v0 in self.graph.vertices['V1'])
        self.assertTrue(v1 in self.graph.vertices['V0'])

    def test_bfs(self):
        self.graph.add_vertex('V1')
        self.graph.add_vertex('V2')
        self.graph.add_vertex('V3')
        self.graph.add_vertex('V4')
        self.graph.add_vertex('V5', ['V3'])
        self.graph.add_vertex('V6')
        self.graph.add_vertex('V7', ['V6', 'V1'])
        self.graph.add_edge('V1', 'V2', False)
        self.graph.add_edge('V2', 'V4', False)
        self.graph.add_edge('V2', 'V3', False)
        self.graph.add_edge('V3', 'V5')
        self.graph.add_edge('V4', 'V7', False)
        self.graph.add_edge('V4', 'V6', False)
        bfs = self.graph.search('V1', 'bfs')
        # Getting different results because of the sets -> can't control order
        if (bfs == ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7']) or (
                bfs == ['V1', 'V2', 'V4', 'V3', 'V6', 'V7', 'V5']) or (
                bfs == ['V1', 'V2', 'V4', 'V3', 'V7', 'V6', 'V5']):
            correct_path = True
        else:
            correct_path = False
        self.assertTrue(correct_path)

    def test_dfs(self):
        self.graph.add_vertex('V1')
        self.graph.add_vertex('V2')
        self.graph.add_vertex('V3')
        self.graph.add_vertex('V4', ['V3'])
        self.graph.add_vertex('V5')
        self.graph.add_vertex('V6', ['V3'])
        self.graph.add_vertex('V7', ['V6', 'V1'])
        self.graph.add_edge('V1', 'V2', False)
        self.graph.add_edge('V2', 'V5', False)
        self.graph.add_edge('V2', 'V3', False)
        self.graph.add_edge('V3', 'V4', False)
        self.graph.add_edge('V5', 'V7', False)
        self.graph.add_edge('V5', 'V6', False)
        dfs = self.graph.search('V1', 'dfs')
        # Getting different results because of the sets -> can't control order
        if (dfs == ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7']) or (
                dfs == ['V1', 'V2', 'V3', 'V4', 'V5', 'V7', 'V6']) or (
                dfs == ['V1', 'V2', 'V5', 'V6', 'V7', 'V3', 'V4']) or (
                dfs == ['V1', 'V2', 'V5', 'V7', 'V6', 'V3', 'V4']) or (
                dfs == ['V1', 'V2', 'V5', 'V6', 'V3', 'V4', 'V7']
                ):
            correct_path = True
        else:
            correct_path = False
        self.assertTrue(correct_path)


if __name__ == '__main__':
    unittest.main()
