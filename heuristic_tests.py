import unittest
from board import Board
from main_script import heuristic_1
from main_script import heuristic_2


class HeuristicTests(unittest.TestCase):

    def test_h2_complete_board(self):
        board = Board([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0])
        heuristic_val = heuristic_2(board)
        self.assertEqual(0, heuristic_val)

    def test_h2_row_swaps(self):
        board = Board([1, 3, 2, 4, 6, 5, 7, 8, 9, 10, 0, 11])
        heuristic_val = heuristic_2(board)
        self.assertEqual(58, heuristic_val)

    def test_h2_false_solution(self):
        board = Board([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        heuristic_val = heuristic_2(board)
        self.assertEqual(79, heuristic_val)
    
    def test_h1_complete_board(self):
        board = Board([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0])
        heuristic_val = heuristic_1(board)
        self.assertEqual(0, heuristic_val)

    def test_h1_invalid_column(self):
        board = Board([1, 2, 3, 4, 5, 6, 7, 0, 9, 10, 11, 8])
        heuristic_val = heuristic_1(board)
        self.assertEqual(217, heuristic_val)

    def test_h1_invalid_rows(self):
        board = Board([1, 2, 3, 7, 5, 6, 0, 4, 9, 10, 11, 8])
        heuristic_val = heuristic_1(board)
        self.assertEqual(334, heuristic_val)


if __name__ == '__main__':
    unittest.main()
