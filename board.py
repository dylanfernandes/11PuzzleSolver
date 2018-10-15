from copy import deepcopy

class Board:

    # DEF here is short for "default"
    DEF_ROW_SIZE = 4
    DEF_COL_SIZE = 3
    SPACE_TOKEN = 0

    def __init__(self, config, row_size=DEF_ROW_SIZE, col_size=DEF_COL_SIZE):
        self.elements = config
        self.row_size = row_size
        self.col_size = col_size
        self.size = self.row_size * self.col_size
        if config and len(config) == self.size:
            self.findSpace()
            self.determineMoves()

    def findSpace(self):
        index = 0
        for i in self.elements:
            if i == self.SPACE_TOKEN:
                break
            index = index + 1
        self.spacePos = index
        return index

    def determineMoves(self):
        self.moves = []
        left = False
        right = False
        up = False
        down = False
        #space not in top row
        if self.spacePos > self.row_size - 1:
            up = True
        #space not at bottom
        if self.spacePos < self.row_size * (self.col_size - 1):
            down = True
        #left and right check
        if self.spacePos % self.row_size != self.row_size - 1:
            right = True
        if self.spacePos % self.row_size != 0:
            left = True
        #generate list of moves according to precedence
        if up:
            self.moves.append(self.spacePos - self.row_size)
            if right:
                self.moves.append(self.spacePos + 1 - self.row_size)
        if right:
            self.moves.append(self.spacePos + 1)
            if down:
                self.moves.append(self.spacePos + 1 + self.row_size)
        if down:
            self.moves.append(self.spacePos + self.row_size)
            if left:
                self.moves.append(self.spacePos - 1 + self.row_size)
        if left:
            self.moves.append(self.spacePos - 1)
            if up:
                self.moves.append(self.spacePos - 1 - self.row_size)
        return self.moves

    def makeMove(self, location):
        if location in self.moves:
            temp = self.elements[location]
            self.elements[location] = self.SPACE_TOKEN
            self.elements[self.spacePos] = temp
            self.spacePos = location
            self.determineMoves()
            return True
        return False

    def getMoveConfig(self, location):
        if location in self.moves:
            config = self.elements[:]
            temp = config[location]
            config[location] = self.SPACE_TOKEN
            config[self.spacePos] = temp
        return Board(config)

    def getAllConfigs(self):
        configs = []
        for move in self.moves:
            configs.append(self.getMoveConfig(move))
        return configs


    def printBoard(self):
        print self.elements

    #Takes index as parameter and returns the corresponding row,index starts at 0
    def getColumn(self, num):
        column = []
        index = num
        for i in range(0, self.col_size): #3 values per column
            column.append(self.elements[index])
            index = index + self.row_size #next column starts 4 elements later
        return column

    #Takes index as parameter and returns the corresponding row, index sarts at 0
    def getRow(self, num):
        row = []
        start = num * self.row_size
        for i in range(0, self.row_size):
            row.append(self.elements[start+i])
        return row

    def getElementRow(self, elVal):
        ind = self.elements.index(elVal)
        elRow = ind / (self.row_size)
        return self.getRow(elRow)

    def getElementColumn(self, elVal):
        ind = self.elements.index(elVal)
        elCol = ind % (self.row_size)
        return self.getColumn(elCol)

    def getElements(self):
        return self.elements

    def getRowSize(self):
        return self.row_size

    def getColSize(self):
        return self.col_size

    def getSize(self):
        return self.size

    # Gets the symbol corresponding to the location on the board
    @staticmethod
    def getPositionLetter(location):
        return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'][location]

    @staticmethod
    def getDefSize():
        return Board.DEF_ROW_SIZE * Board.DEF_COL_SIZE

    # Equality
    def __eq__(self, other):
        return self.elements == other.getElements()

    def __ne__(self, other):
        return not self.__eq__(other)

    # To String
    def __str__(self):
        return str(self.elements)


