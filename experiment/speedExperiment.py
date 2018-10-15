import sys
sys.path.insert(0, '../')
import main_script
import time
from main_script import *

valid_board_0 = Board([2, 0, 3, 4, 5, 1, 6, 8, 9, 10, 11, 7])
valid_board_1 = Board([1, 6, 3, 4, 9, 10, 2, 8, 5, 11, 0, 7])
valid_board_2 = Board([9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7, 8])
boards = [valid_board_0, valid_board_1, valid_board_2]
heuristics = [heuristic_1, heuristic_2]
search_functions = [best_first_search, a_star] 
def main():
    compare_heuristics()
    #H1_MODIFIER = 
    #H2_MODIFIER =
def compare_heuristics():
    for heuristic in heuristics:
        for search_function in search_functions:
            print `search_function.__name__` + " with " + `heuristic.__name__` + "on:"
            for board in boards:
                start = time.time()
                search_function(board, heuristic)
                end = time.time()
                print `board.elements` + "\nTime:  " +  `end - start`
                print "-------------------------"


if __name__ == '__main__':
        main()
