import unittest
from bidirectional_search import bidi_search as bidirectional_search


class TestCaseOne(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = {
            0: {1, 2},
            1: {0, 2, 3, 4},
            2: {0, 1, 4, 6},
            3: {1, 5},
            4: {1, 2, 5},
            5: {3, 4},
            6: {2},
        }
        self.zero_to = {
            0: [
                [0]
            ],
            1: [
                [0, 1],
            ],
            2: [
                [0, 2],
            ],
            3: [
                [0, 1, 3],
            ],
            4: [
                [0, 1, 4],
                [0, 2, 4],
            ],
            5: [
                [0, 1, 3, 5],
                [0, 1, 4, 5],
                [0, 2, 4, 5],
            ],
            6: [
                [0, 2, 6],
            ],
        }

    def make_tester_zero_to(self, end):
        actual = bidirectional_search(self.graph, 0, end)
        fail_msg = f"Returned result {actual} was not a valid possibility {self.zero_to[end]}"
        self.assertIn(actual, self.zero_to[end], fail_msg)

    def test_valid_zero_to_self(self):
        self.make_tester_zero_to(0)

    def test_valid_zero_to_one(self):
        self.make_tester_zero_to(1)

    def test_valid_zero_to_two(self):
        self.make_tester_zero_to(2)

    def test_valid_zero_to_three(self):
        self.make_tester_zero_to(3)

    def test_valid_zero_to_four(self):
        self.make_tester_zero_to(4)

    # @unittest.skip
    def test_valid_zero_to_five(self):
        self.make_tester_zero_to(5)

    def test_zero_to_six(self):
        self.make_tester_zero_to(6)


if __name__ == '__main__':
    unittest.main()
