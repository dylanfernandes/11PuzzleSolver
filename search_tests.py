import unittest
from board import Board
from main_script import *


class SearchTests(unittest.TestCase):

    valid_board_1 = Board([2, 0, 3, 4, 5, 1, 6, 8, 9, 10, 11, 7])
    valid_board_2 = Board([1, 6, 3, 4, 9, 10, 2, 8, 5, 11, 0, 7])
    valid_board_3 = Board([9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7, 8])

    def test_best_search_h2_complete_board(self):
        board = Board([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0])
        solution_node = best_first_search(board, heuristic_2)
        solution = get_solution_path(solution_node)
        self.assertEqual(0, len(solution))
        self.assertEqual([], solution)

    def test_best_search_h2_valid_solution_1(self):
        solution_node = best_first_search(SearchTests.valid_board_1, heuristic_2)
        solution = get_solution_path(solution_node)
        self.assertGreater(len(solution), 0)

    def test_best_search_h2_valid_solution_2(self):
        solution_node = best_first_search(SearchTests.valid_board_2, heuristic_2)
        solution = get_solution_path(solution_node)
        self.assertGreater(len(solution), 0)

    def test_best_search_h2_valid_solution_3(self):
        solution_node = best_first_search(SearchTests.valid_board_3, heuristic_2)
        solution = get_solution_path(solution_node)
        self.assertGreater(len(solution), 0)


if __name__ == '__main__':
    unittest.main()
