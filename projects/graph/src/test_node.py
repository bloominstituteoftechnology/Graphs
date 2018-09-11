import unittest
from node import Node


class NodeTests(unittest.TestCase):
    def setUp(self):
        self.node = Node(5,4,.2)  # Instantiate your node

    def test_instantiation(self):
        self.assertEqual(self.node.x, 5)
        self.assertEqual(self.node.y, 4)
        self.assertEqual(self.node.radius, .2)

if __name__ == '__main__':
    unittest.main()