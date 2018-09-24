
class TreeNode:

    def __init__(self, data, parent, left_child, right_child):
        self.data = data
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    def __init__(self, data, parent):
        self.__init__(self, data, parent, None, None)

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_left_child(self, left_child):
        self.left_child = left_child

    def get_left_child(self):
        return self.left_child

    def set_right_child(self, right_child):
        self.right_child = right_child

    def get_right_child(self):
        return self.right_child

