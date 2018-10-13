import unittest
from main_script import *
from board import Board

class Test_Main(unittest.TestCase):
    def test_dfs(self):
        vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0]
        board = Board(vals)
        depth_first_search(board)

if __name__ == '__main__':
        unittest.main()
