import unittest
import main_script
from main_script import *


class Puzzle11SolverTests(unittest.TestCase):

    board_size = Board.row_size * Board.col_size

    # Input tests
    def test_correct_input(self):
        # Replace the "raw_input" function with a lambda that simply returns a string that we specify
        # this is how input is mocked in these tests
        main_script.raw_input = lambda _: '3 2 1 4 6 7 5 8 9 0 10 11'
        board = input_board()
        self.assertIsNotNone(board)

    def test_invalid_input_no_spaces(self):
        main_script.raw_input = lambda _: '32146758901011'
        board = input_board()
        self.assertIsNone(board)

    def test_invalid_input_non_int(self):
        main_script.raw_input = lambda _: '3 2 1 4 6 7 5 8 9 0 1f 11'
        board = input_board()
        self.assertIsNone(board)

    def test_incorrect_size_small(self):
        main_script.raw_input = lambda _: '3 2 1 4 6 7 5 8 9 0'
        board = input_board()
        self.assertIsNone(board)

    def test_incorrect_size_large(self):
        main_script.raw_input = lambda _: '3 2 1 4 6 7 5 8 9 0 10 11 12 13'
        board = input_board()
        self.assertIsNone(board)

    def test_incorrect_input_small(self):
        main_script.raw_input = lambda _: '-3 2 1 4 6 7 5 8 9 0 10 11'
        board = input_board()
        self.assertIsNone(board)

    def test_incorrect_input_large(self):
        main_script.raw_input = lambda _: '23 2 1 4 6 7 5 8 9 0 10 11'
        board = input_board()
        self.assertIsNone(board)

    def test_duplicate_nums(self):
        # 3 is duplicated here
        main_script.raw_input = lambda _: '3 2 1 4 6 3 5 8 9 0 10 11'
        board = input_board()
        self.assertIsNone(board)


if __name__ == '__main__':
    unittest.main()
