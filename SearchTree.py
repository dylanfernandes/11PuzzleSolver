
class TreeNode:

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []
        self.heuristic_value = 0

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def create_and_add_child(self, data):
        tree_node = TreeNode(data)
        tree_node.set_parent(self)
        self.children.append(tree_node)

    def add_child(self, tree_node):
        tree_node.set_parent(self)
        self.children.append(tree_node)

    def add_children(self, tree_nodes):
        for tree_node in tree_nodes:
            tree_node.set_parent(self)
        self.children.extend(tree_nodes)

    def get_children(self):
        return self.children

    def set_heuristic_value(self, heuristic_value):
        self.heuristic_value = heuristic_value

    def get_heuristic_value(self):
        return self.heuristic_value

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def __str__(self):
        return self.data.__str__()

    # Comparision methods - based on heuristic_value
    def __lt__(self, other):
        return self.heuristic_value < other.get_heursitic_value()

    def __le__(self, other):
        return self.heuristic_value <= other.get_heursitic_value()

    def __gt__(self, other):
        return self.heuristic_value > other.get_heursitic_value()

    def __ge__(self, other):
        return self.heuristic_value >= other.get_heursitic_value()

    def __eq__(self, other):
        return self.heuristic_value == other.get_heursitic_value()

    def __ne__(self, other):
        return self.heuristic_value != other.get_heursitic_value()
