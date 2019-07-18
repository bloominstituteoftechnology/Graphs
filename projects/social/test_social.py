import unittest
from social import SocialGraph

class Test(unittest.TestCase):
  def test_social_graph(self):
    # Instatiate Social Graph
    sg = SocialGraph()

    # Add Users
    sg.addUser(1)
    sg.addUser(2)
    sg.addUser(3)
    sg.addUser(4)
    sg.addUser(5)
    sg.addUser(6)
    sg.addUser(7)
    sg.addUser(8)
    sg.addUser(9)
    sg.addUser(10)

    # Add Friendships
    sg.addFriendship(1, 8)
    sg.addFriendship(1, 10)
    sg.addFriendship(1, 5)

    sg.addFriendship(2, 10)
    sg.addFriendship(2, 5)
    sg.addFriendship(2, 7)

    sg.addFriendship(3, 4)

    sg.addFriendship(4, 9)

    sg.addFriendship(5, 8)

    sg.addFriendship(6, 10)

    # Test Friendships
    correct_friendships = {1: {8, 10, 5}, 2: {10, 5, 7}, 3: {4}, 4: {9, 3}, 5: {8, 1, 2}, 6: {10}, 7: {2}, 8: {1, 5}, 9: {4}, 10: {1, 2, 6}}
    self.assertEqual(sg.friendships, correct_friendships)

    # Test Connections
    correct_connections = {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}
    self.assertEqual(sg.getAllSocialPaths(1), correct_connections)

if __name__ == '__main__':
  unittest.main()