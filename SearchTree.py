
class TreeNode:

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []
        self.heuristic_value = 0
        self.total_cost_value = 0

    # The data will be an (integer, character, board) tuple
    # The integer will be the numerical value of the piece that has moved
    # The character will be its corresponding letter position of the piece prior to it being moved
    # The board will be the board_config after the move has been made
    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def create_and_add_child(self, data):
        self.create_and_add_child_with_cost(data, 0, 0)

    def create_and_add_child_with_cost(self, data, heuristic_value, cost):
        tree_node = TreeNode(data)
        tree_node.set_parent(self)
        tree_node.set_heuristic_value(heuristic_value)
        tree_node.set_total_cost_value(self.total_cost_value + cost)
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

    def set_total_cost_value(self, total_cost_value):
        self.total_cost_value = total_cost_value

    def get_total_cost_value(self):
        return self.total_cost_value

    def get_algo_a_value(self):
        """
        Represents the function f(n) = h(n) + g(n)
        :return: the heuristic value plus the total cost of this node.
        """
        return self.total_cost_value + self.heuristic_value

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def __str__(self):
        return self.data.__str__()

    # Comparision methods - based on heuristic_value
    def __cmp__(self, other):
        return (self.get_algo_a_value() > other.get_algo_a_value()) \
               - (self.get_algo_a_value() < other.get_algo_a_value())

    def __eq__(self, other):
        return self.get_data() == other.get_data() \
               and self.get_heuristic_value() == other.get_heuristic_value()

    def __ne__(self, other):
        return not self.__eq__(other)
