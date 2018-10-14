import sys
sys.path.insert(0, '../')
import unittest
from main_script import *
from board import Board

class Test_Main(unittest.TestCase):
    def test_dfs(self):
        vals = [1, 2, 3, 4, 5, 6, 7, 0, 9, 10, 11, 8]
        board = Board(vals)
        self.assertEqual(True, depth_first_search(board))

    def test_is_node_in_node_list(self):
        node_list = []
        node1 = TreeNode(('a', Board([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0])))
        node2 = TreeNode(('b',Board([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 11])))
        node3 = TreeNode(('a',Board([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11])))
        node_list.append(node1)
        node_list.append(node2)
        self.assertEqual(False, is_node_in_node_list(node3, node_list))
        node_list.append(node3)
        self.assertEqual(True, is_node_in_node_list(node3, node_list))
if __name__ == '__main__':
        unittest.main()
