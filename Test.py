import unittest
from HyperSudoku import *

#####################################################################
#                                                                   #
#   Individial tests can be run as follows:                         #
#      python3 Test.py TestHyperSudoku.test_One      (etc)          #
#                                                                   #
#####################################################################


class TestHyperSudoku(unittest.TestCase):

    # This should be unsolvable.
    #           Time on my solution ~0.68s
    def test_Unsolvable_One(self):
        grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                [3, 0, 0, 0, 0, 5, 0, 0, 8],
                [9, 6, 4, 0, 7, 8, 2, 0, 0],
                [0, 0, 0, 0, 3, 0, 0, 2, 0],
                [7, 0, 8, 2, 0, 0, 1, 0, 3],
                [0, 4, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 6, 4, 0, 0, 0, 2],
                [0, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertIsNone(HyperSudoku.solve(grid))

    # Valid Hyper-Sudoku Grid.
    #           Time on my solution < 0.1s
    def test_One(self):
        grid = [[0, 0, 0, 0, 9, 0, 7, 0, 0],
                [0, 6, 1, 0, 0, 0, 0, 4, 0],
                [0, 0, 0, 0, 0, 2, 0, 0, 3],
                [0, 0, 7, 4, 8, 0, 0, 0, 0],
                [0, 8, 0, 0, 0, 0, 6, 0, 0],
                [0, 0, 3, 0, 0, 0, 5, 0, 0],
                [0, 0, 0, 5, 0, 0, 2, 0, 0],
                [9, 0, 0, 1, 0, 0, 0, 0, 0],
                [5, 0, 2, 0, 0, 0, 0, 8, 6]]

        soln = [[8, 3, 4, 6, 9, 1, 7, 5, 2],
                [2, 6, 1, 3, 5, 7, 8, 4, 9],
                [7, 5, 9, 8, 4, 2, 1, 6, 3],
                [6, 2, 7, 4, 8, 5, 3, 9, 1],
                [1, 8, 5, 9, 7, 3, 6, 2, 4],
                [4, 9, 3, 2, 1, 6, 5, 7, 8],
                [3, 4, 8, 5, 6, 9, 2, 1, 7],
                [9, 7, 6, 1, 2, 8, 4, 3, 5],
                [5, 1, 2, 7, 3, 4, 9, 8, 6]]

        self.assertEqual(HyperSudoku.solve(grid), soln)

    # Valid Hyper-Sudoku Grid.
    #           Time on my solution < 0.1s.
    def test_Two(self):
        grid = [[0, 0, 6, 0, 9, 4, 0, 0, 0],
                [0, 0, 0, 0, 5, 0, 8, 9, 0],
                [1, 8, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 2, 0, 0, 0, 0, 3, 0],
                [0, 0, 0, 9, 0, 5, 0, 2, 0],
                [3, 0, 0, 0, 2, 0, 0, 0, 7],
                [6, 0, 3, 0, 0, 0, 0, 7, 0],
                [0, 9, 0, 0, 0, 0, 0, 0, 0],
                [0, 2, 0, 0, 0, 0, 0, 0, 0]]

        soln = [[5, 3, 6, 8, 9, 4, 7, 1, 2],
                [2, 7, 4, 1, 5, 6, 8, 9, 3],
                [1, 8, 9, 3, 7, 2, 5, 4, 6],
                [9, 5, 2, 6, 8, 7, 1, 3, 4],
                [7, 4, 1, 9, 3, 5, 6, 2, 8],
                [3, 6, 8, 4, 2, 1, 9, 5, 7],
                [6, 1, 3, 5, 4, 8, 2, 7, 9],
                [8, 9, 7, 2, 1, 3, 4, 6, 5],
                [4, 2, 5, 7, 6, 9, 3, 8, 1]]

        self.assertEqual(HyperSudoku.solve(grid), soln)


if __name__ == "__main__":
    unittest.main()
