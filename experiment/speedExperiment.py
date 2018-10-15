import sys
sys.path.insert(0, '../')
import main_script
import time
from main_script import *

mix_1= Board([2, 0, 3, 4, 5, 1, 6, 8, 9, 10, 11, 7])
mix_2 = Board([1, 6, 3, 4, 9, 10, 2, 8, 5, 11, 0, 7])
row_shuffle = Board([9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7, 8])
column_shuffle = Board([4, 3, 2, 1, 8, 7, 6, 5, 0, 11, 10 ,9])
bad_column = Board([1, 2, 3, 8, 5, 6, 7, 0, 9, 10, 11, 4])
bad_row = Board([1, 2, 3, 4, 5, 6, 7, 8, 11, 0, 10, 9])
search_functions = [a_star]  # best_first_search, 
def main():
    compare_heuristics()
    modify_heuristic_1()
    modify_heuristic_2()

def test(heuristics, boards, board_names):
    for heuristic in heuristics:
        for search_function in search_functions:
            print `search_function.__name__` + " with " + `heuristic.__name__` + "on:"
            boad_name_index = 0
            for board in boards:
                start = time.time()
                sol = search_function(board, heuristic)
                end = time.time()
                print `board_names[boad_name_index]` + "\nTime:  " +  `end - start`
                print "-------------------------"
                boad_name_index = boad_name_index + 1

def compare_heuristics():
    heuristics = [heuristic_1, heuristic_2]
    boards = [mix_1, mix_2, row_shuffle, bad_column]
    board_names = ["mix_1", "mix_2", "row_shuffle","bad_column"]
    test(heuristics, boards, board_names)

def modify_heuristic_1():
    heuristics = [heuristic_1]
    boards = [mix_1, mix_2, row_shuffle, bad_column]
    board_names = ["mix_1", "mix_2", "row_shuffle","bad_column"]
    test(heuristics, boards, board_names)
    main_script.H1_MODIFIER = [1,2,3,4]
    print "Modifier applied: " + `main_script.H1_MODIFIER`
    test(heuristics, boards, board_names)
    main_script.H1_MODIFIER = []

def modify_heuristic_2():
        heuristics = [heuristic_2]
        boards = [mix_1, mix_2, row_shuffle, bad_column, bad_row]
        board_names = ["mix_1", "mix_2", "row_shuffle", "bad_column", "bad_row"]
        test(heuristics, boards, board_names)
        main_script.H2_MODIFIER = [0, 1]
        print "Modifier applied: " + `main_script.H2_MODIFIER`
        test(heuristics, boards, board_names)
        main_script.H2_MODIFIER = []          

if __name__ == '__main__':
        main()
