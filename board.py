from copy import deepcopy

class Board:
    SIZE = 12
    ROWSIZE = 4
    COLSIZE = 3
    SPACETOKEN = 0

    def __init__(self, config):
        self.elements = config
        if config and len(config) == self.SIZE:
            self.findSpace()
            self.determineMoves()

    def findSpace(self):
        index = 0
        for i in self.elements:
            if i == self.SPACETOKEN:
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
        if self.spacePos > self.ROWSIZE - 1:
            up = True
        #space not at bottom
        if self.spacePos < self.ROWSIZE * (self.COLSIZE - 1):
            down = True
        #left and right check
        if self.spacePos % self.ROWSIZE != self.ROWSIZE - 1:
            right = True
        if self.spacePos % self.ROWSIZE != 0:
            left = True
        #generate list of moves according to precedence
        if up:
            self.moves.append(self.spacePos - self.ROWSIZE)
            if right:
                self.moves.append(self.spacePos + 1 - self.ROWSIZE)
        if right:
            self.moves.append(self.spacePos + 1)
            if down:
                self.moves.append(self.spacePos + 1 + self.ROWSIZE)
        if down:
            self.moves.append(self.spacePos + self.ROWSIZE)
            if left:
                self.moves.append(self.spacePos - 1 + self.ROWSIZE)
        if left:
            self.moves.append(self.spacePos - 1)
            if up:
                self.moves.append(self.spacePos - 1 - self.ROWSIZE) 
        return self.moves

    def makeMove(self, location):
        if location in self.moves:
            temp = self.elements[location]
            self.elements[location] = self.SPACETOKEN
            self.elements[self.spacePos] = temp
            self.spacePos = location
            self.determineMoves()
            return True
        return False

    def getMoveConfig(self, location):
        if location in self.moves:
            config = self.elements[:]
            temp = config[location]
            config[location] = self.SPACETOKEN
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
        for i in range(0,self.COLSIZE): #3 values per column
            column.append(self.elements[index])
            index = index + self.ROWSIZE #next column starts 4 elements later
        return column

    #Takes index as parameter and returns the corresponding row, index sarts at 0
    def getRow(self, num):
        row = []
        start = num * self.ROWSIZE
        for i in range(0, self.ROWSIZE):
            row.append(self.elements[start+i])
        return row

    def getElementRow(self, elVal):
        ind = self.elements.index(elVal)
        elRow = ind / (self.ROWSIZE)
        return self.getRow(elRow)

    def getElementColumn(self, elVal):
        ind = self.elements.index(elVal)
        elCol = ind % (self.ROWSIZE)
        return self.getColumn(elCol)

    def getElements(self):
        return self.elements

    # Gets the symbol corresponding to the input element value
    def getElementLetter(self, elVal):
        index = self.elements.index(elVal)
        return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'][index]

    def __eq__(self, other):
        return self.elements == other.getElements()


