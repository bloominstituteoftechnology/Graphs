import unittest

from social import SocialGraph


class SocialNetworkTest(unittest.TestCase):

    def test_get_all_social_paths(self):
        social_graph = SocialGraph()

        readme_graph = {
            1: {8, 10, 5},
            2: {10, 5, 7},
            3: {4},
            4: {9, 3},
            5: {8, 1, 2},
            6: {10},
            7: {2},
            8: {1, 5},
            9: {4},
            10: {1, 2, 6}
        }

        for key in readme_graph:
            social_graph.add_user(key)

        for key in readme_graph:
            social_graph.add_friendships(key, *readme_graph[key])

        actual_result = social_graph.get_all_social_paths(1)
        expected_result = {1: [1], 8: [1, 8], 10: [1, 10], 5: [1, 5], 2: [1, 10, 2], 6: [1, 10, 6], 7: [1, 10, 2, 7]}
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
