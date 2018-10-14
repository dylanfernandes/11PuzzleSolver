import sys
sys.path.insert(0, '../')
import unittest
from SearchTree import TreeNode

class TestTreeNode(unittest.TestCase):

    def testAddSingleChild(self):
        tree = TreeNode(15)
        child1 = TreeNode(1)
        tree.add_child(child1)
        treeChildren = tree.get_children()
        child = treeChildren[0]
        self.assertEqual(len(treeChildren), 1)
        self.assertEqual(child.get_data(), 1)
        self.assertEqual(child.get_parent().get_data(), 15)

    def testAddChildren(self):
        tree = TreeNode(15)
        children = []
        child1 = TreeNode(1)
        child2 = TreeNode(2)
        child3 = TreeNode(3)
        children.insert(0, child1)
        children.insert(1, child2)
        children.insert(2, child3)
        tree.add_children(children)
        treeChildren = tree.get_children()
        retChild1 = treeChildren[0]
        retChild2 = treeChildren[1]
        retChild3 = treeChildren[2]
        self.assertEqual(len(treeChildren), 3)
        self.assertEqual(retChild1.get_data(), 1)
        self.assertEqual(retChild1.get_parent().get_data(), 15)
        self.assertEqual(retChild2.get_data(), 2)
        self.assertEqual(retChild2.get_parent().get_data(), 15)
        self.assertEqual(retChild3.get_data(), 3)
        self.assertEqual(retChild3.get_parent().get_data(), 15)

if __name__ == '__main__':
        unittest.main()
