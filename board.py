class Board:
    SIZE = 12
    ROWSIZE = 4
    COLSIZE = 3
    SPACETOKEN = 0
    moves = []
    elements = []
    spacePos = 0

    def __init__(self, e0 = 0, e1 = 0, e2 = 0, e3 = 0, e4 = 0, e5 = 0, e6 = 0, e7 = 0, e8 = 0, e9 = 0, e10 = 0, e11 = 0):
        self.elements.insert(0 ,e0)
        self.elements.insert(1 ,e1)
        self.elements.insert(2 ,e2)
        self.elements.insert(3 ,e3)
        self.elements.insert(4 ,e4)
        self.elements.insert(5 ,e5)
        self.elements.insert(6 ,e6)
        self.elements.insert(7 ,e7)
        self.elements.insert(8 ,e8)
        self.elements.insert(9 ,e9)
        self.elements.insert(10 ,e10)
        self.elements.insert(11 ,e11)
        self.findSpace()
        self.getMoves()

    def findSpace(self):
        index = 0
        for i in self.elements:
            if i == self.SPACETOKEN:
                break
            index = index + 1
        self.spacePos = index
        return index

    def getMoves(self):
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
            self.elements[self.spacePos]  = temp
            self.spacePos = location
            self.getMoves()
            return True
        return False


    def printBoard(self):
        print self.elements

    #index starts at 0
    def getColumn(self, num):
        column = []
        index = num
        for i in range(0,self.COLSIZE): #3 values per column
            column.insert(i, self.elements[index])
            index = index + self.ROWSIZE #next column starts 4 elements later
        return column

    #index sarts at 0
    def getRow(self, num):
        row = []
        start = num * self.ROWSIZE
        for i in range(0,self.ROWSIZE):
            row.insert(i, self.elements[start+i])
        return row

