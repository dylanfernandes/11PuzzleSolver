import unittest
from board import Board

class TestBoard(unittest.TestCase):
    board = Board(8,1,2,3,4,5,6,7,0,9,10,11)

    def testBoardInitialization(self):
        self.assertEqual(len(self.board.elements), 12)
        self.assertEqual(self.board.elements[0], 8)
        self.assertEqual(self.board.findSpace(), 8)

    def testGetRow(self):
        row = self.board.getRow(1)
        self.assertEqual(len(row), 4)
        self.assertEqual(row[0], 4)
        self.assertEqual(row[1], 5)
        self.assertEqual(row[2], 6)
        self.assertEqual(row[3], 7)

    def testGetColumn(self):
        col = self.board.getColumn(1)
        self.assertEqual(len(col), 3)
        self.assertEqual(col[0], 1)
        self.assertEqual(col[1], 5)
        self.assertEqual(col[2], 9)

    def testPossibleMoves(self):
        moves = self.board.getMoves()
        self.assertEqual(len(moves), 3)
        self.assertEqual(moves[0], 4)
        self.assertEqual(moves[1], 5)
        self.assertEqual(moves[2], 9)

    def testMakeMove(self):
        self.assertEqual(self.board.makeMove(4), True)
        self.assertEqual(self.board.elements, [8,1,2,3,0,5,6,7,4,9,10,11])
        self.assertEqual(self.board.makeMove(8), True)
        self.assertEqual(self.board.elements, [8,1,2,3,4,5,6,7,0,9,10,11])
        self.assertEqual(self.board.makeMove(1), False)

if __name__ == '__main__':
        unittest.main()
