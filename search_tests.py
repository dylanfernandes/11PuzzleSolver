import unittest
import random
from main_script import *
from datetime import datetime


class SearchTests(unittest.TestCase):

    # Constants
    GOAL_STATE_HEURISTIC_VAL = 0
    GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]
    BOARD_TUPLE_INDEX = 1

    # Test variables
    valid_board_1 = Board([2, 0, 3, 4, 5, 1, 6, 8, 9, 10, 11, 7])
    valid_board_2 = Board([1, 6, 3, 4, 9, 10, 2, 8, 5, 11, 0, 7])
    valid_board_3 = Board([9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7, 8])
    board_size = Board.ROWSIZE * Board.COLSIZE

    # Best First Search - Heuristic 2
    def test_best_search_h2_complete_board(self):
        board = Board(GOAL_STATE)
        solution_node = best_first_search(board, heuristic_2)
        solution = get_solution_path(solution_node)
        self.assertEqual(self.GOAL_STATE_HEURISTIC_VAL, solution_node.get_heuristic_value())
        self.assertEqual(self.GOAL_STATE, solution_node.get_data()[self.BOARD_TUPLE_INDEX].getElements())
        self.assertEqual([], solution)

    def test_best_search_h2_valid_solution_1(self):
        solution_node = best_first_search(SearchTests.valid_board_1, heuristic_2)
        solution = get_solution_path(solution_node)
        self.assertEqual(self.GOAL_STATE_HEURISTIC_VAL, solution_node.get_heuristic_value())
        self.assertEqual(self.GOAL_STATE, solution_node.get_data()[self.BOARD_TUPLE_INDEX].getElements())
        self.assertGreater(len(solution), 0)

    def test_best_search_h2_valid_solution_2(self):
        solution_node = best_first_search(SearchTests.valid_board_2, heuristic_2)
        solution = get_solution_path(solution_node)
        self.assertEqual(self.GOAL_STATE_HEURISTIC_VAL, solution_node.get_heuristic_value())
        self.assertEqual(self.GOAL_STATE, solution_node.get_data()[self.BOARD_TUPLE_INDEX].getElements())
        self.assertGreater(len(solution), 0)

    def test_best_search_h2_valid_solution_3(self):
        solution_node = best_first_search(SearchTests.valid_board_3, heuristic_2)
        solution = get_solution_path(solution_node)
        self.assertEqual(self.GOAL_STATE_HEURISTIC_VAL, solution_node.get_heuristic_value())
        self.assertEqual(self.GOAL_STATE, solution_node.get_data()[self.BOARD_TUPLE_INDEX].getElements())
        self.assertGreater(len(solution), 0)

    def test_best_search_h2_random_board(self):
        random_board = self.generate_random_board()
        random_board.printBoard()
        solution_node = best_first_search(random_board, heuristic_2)
        solution = get_solution_path(solution_node)
        self.assertEqual(self.GOAL_STATE_HEURISTIC_VAL, solution_node.get_heuristic_value())
        self.assertEqual(self.GOAL_STATE, solution_node.get_data()[self.BOARD_TUPLE_INDEX].getElements())
        self.assertGreater(len(solution), 0)

    # A* - Heuristic 2
    def test_a_star_h2_complete_board(self):
        board = Board(GOAL_STATE)
        solution_node = a_star(board, heuristic_2)
        solution = get_solution_path(solution_node)
        self.assertEqual(self.GOAL_STATE_HEURISTIC_VAL, solution_node.get_heuristic_value())
        self.assertEqual(self.GOAL_STATE, solution_node.get_data()[self.BOARD_TUPLE_INDEX].getElements())
        self.assertEqual([], solution)

    def test_a_star_h2_valid_solution_1(self):
        solution_node = a_star(SearchTests.valid_board_1, heuristic_2)
        solution = get_solution_path(solution_node)
        self.assertEqual(self.GOAL_STATE_HEURISTIC_VAL, solution_node.get_heuristic_value())
        self.assertEqual(self.GOAL_STATE, solution_node.get_data()[self.BOARD_TUPLE_INDEX].getElements())
        self.assertGreater(len(solution), 0)

    def test_a_star_h2_valid_solution_2(self):
        solution_node = a_star(SearchTests.valid_board_2, heuristic_2)
        solution = get_solution_path(solution_node)
        self.assertGreater(len(solution), 0)

    def test_a_star_h2_valid_solution_3(self):
        solution_node = a_star(SearchTests.valid_board_3, heuristic_2)
        solution = get_solution_path(solution_node)
        self.assertEqual(self.GOAL_STATE_HEURISTIC_VAL, solution_node.get_heuristic_value())
        self.assertEqual(self.GOAL_STATE, solution_node.get_data()[self.BOARD_TUPLE_INDEX].getElements())
        self.assertGreater(len(solution), 0)

    def test_a_star_h2_random_board(self):
        random_board = self.generate_random_board()
        random_board.printBoard()
        solution_node = a_star(random_board, heuristic_2)
        solution = get_solution_path(solution_node)
        self.assertEqual(self.GOAL_STATE_HEURISTIC_VAL, solution_node.get_heuristic_value())
        self.assertEqual(self.GOAL_STATE, solution_node.get_data()[self.BOARD_TUPLE_INDEX].getElements())
        self.assertGreater(len(solution), 0)

    # A* vs BFS
    def test_a_star_vs_bfs_h2_random_board(self):
        random_board = self.generate_random_board()
        print 'BFS'
        random_board.printBoard()
        print
        solution_node_bfs = best_first_search(random_board, heuristic_2)
        solution_bfs = get_solution_path(solution_node_bfs)

        print '\nA*'
        random_board.printBoard()
        print
        solution_node_a_star = a_star(random_board, heuristic_2)
        solution_a_star = get_solution_path(solution_node_a_star)
        print len(solution_bfs), len(solution_a_star)
        self.assertGreater(len(solution_bfs), len(solution_a_star))

    # Utility functions
    def generate_random_board(self):
        random.seed(datetime.now())
        random_board_config = random.sample(range(self.board_size), self.board_size)
        return Board(random_board_config)


if __name__ == '__main__':
    unittest.main()
