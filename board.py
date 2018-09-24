class Board:
    elements = []
    SIZE = 12
    def __init__(self):
        self.elements = [0]*self.SIZE

    def printBoard(self):
        print self.elements
