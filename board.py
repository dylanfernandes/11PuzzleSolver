class Board:
    elements = []
    SIZE = 12
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

    def printBoard(self):
        print self.elements

    def getColumn(self, num):
        column = []
        index = num
        print "index: " + `index`
        print "Length: " + `len(self.elements)`
        print "Element: " + `self.elements[4]`
        for i in range(0,3): #3 values per column
            column.insert(i, self.elements[index])
            index = index + 4 #next column starts 4 elements later
        return column

    def getRow(self, num):
        row = []
        for i in range(0,4):
            row.insert(i, self.elements[num+i])
        return row

