import random
from datetime import datetime
from main_script import *


def expr_main():
    bigger_board_searches()


def bigger_board_searches():

    bigger_board_rows = Board.DEF_ROW_SIZE * 2
    bigger_board_cols = Board.DEF_COL_SIZE * 2
    board_to_solve = Board(generate_random_board_config(bigger_board_rows * bigger_board_cols), bigger_board_rows, bigger_board_cols)

    # Perform all of the searches
    bfs_h1_solution = best_first_search(board_to_solve, heuristic_1)
    print 'See solution in puzzleBFS-h1.txt.\n'

    a_star_h1_solution = a_star(board_to_solve, heuristic_1)
    print 'See solution in puzzleAs-h1.txt.\n'

    bfs_h2_solution = best_first_search(board_to_solve, heuristic_2)
    print 'See solution in puzzleBFS-h2.txt.\n'

    a_star_h2_solution = a_star(board_to_solve, heuristic_2)
    print 'See solution in puzzleAs-h2.txt.\n'

    # Generate the output files
    output_solution_in_file(bfs_h1_solution, 'puzzleBFS-h1.txt')
    output_solution_in_file(a_star_h1_solution, 'puzzleAs-h1.txt')
    output_solution_in_file(bfs_h2_solution, 'puzzleBFS-h2.txt')
    output_solution_in_file(a_star_h2_solution, 'puzzleAs-h2.txt')


def generate_random_board_config(board_size):
    if board_size > 0:
        random.seed(datetime.now())
        random_board_config = random.sample(range(board_size), board_size)
        return random_board_config


if __name__ == '__main__':
    expr_main()
