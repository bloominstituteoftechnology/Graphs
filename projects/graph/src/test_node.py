import unittest
from node import Node


class NodeTests(unittest.TestCase):
    def setUp(self):
        self.node = Node(5,4,.2)  # Instantiate your node

    def test_instantiation(self):
        self.assertEqual(self.node.x, 5)
        self.assertEqual(self.node.y, 4)
        self.assertEqual(self.node.radius, .2)
        self.assertEqual(self.node.id, 0)
        self.node2 = Node(5,4,.2)  # Instantiate your node
        self.assertEqual(self.node.id, 0)
        self.assertEqual(self.node2.id, 1)

    def test_color_methods(self):
        self.assertEqual(self.node.color, 'white')
        self.node.assign_random_color()
        self.assertRegex(self.node.color, r'#[0-9A-F]{6}')

    def test_create_with_random_props(self):
        random_node = Node.create_with_random_props(4,4)
        self.assertGreater(random_node.x, 0)
        self.assertLess(random_node.y, 4)

if __name__ == '__main__':
    unittest.main()