
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

    def get_parent(self):
        return self.parent

    def __str__(self):
        return self.data.__str__()

    def get_path_to_node(self, tree_node_to_find):
        return self._get_path_to_node(self, tree_node_to_find)

    # Gets the shortest path to the tree node
    def _get_path_to_node(self, curr_tree_node, tree_node_to_find):
        if curr_tree_node is tree_node_to_find:
            return curr_tree_node.__str__()
        elif curr_tree_node is None:
            path_left = curr_tree_node.__str__() + self._get_path_to_node(curr_tree_node.left_child, tree_node_to_find)
            path_right = curr_tree_node.__str__() + self._get_path_to_node(curr_tree_node.right_child, tree_node_to_find)
            if len(path_left) > len(path_right):
                return path_left
            else:
                return path_right
        else:
            return ""

