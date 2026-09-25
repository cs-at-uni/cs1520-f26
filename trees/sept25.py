# Announcements:
# * Quiz 2 will be next Wednesday, September 30, covering ]
#   lists, stacks, queues, deques, and recursion
#   * We'll discuss practice problems on Monday


# Repeating (and completing) the tree from sept23.py:
class BinaryTreeNode():
    def __init__(self, element, left, right):
        self._element = element
        self._left = left
        self._right = right

    def getElement(self):
        return self._element
    
    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def setLeft(self, left):
        self._left = left

    def setRight(self, right):
        self._right = right

class BinaryTree():
    def __init__(self):
        self._root = None
        self._size = 0

    # Insert into the tree, maintaining the completeness property
    def insert(self, element):
        pass # we'll come back to this!

# It might be helpful to discuss "tree traversals" first!

    # This function returns a list of the *nodes* in the tree,
    # given in the order they are visited in a preorder traversal
    # (preorder processes a node, then its left, then its right)
    # e.g.: the tree
    #     0
    #    / \
    #   1   4
    #  / \ / \
    # 2  3 5  6
    # would return [0 1 2 3 4 5 6]
    def preorder_traversal(self):
        if self._root is None:
            return []
        else:
            return [self._root] + \
                    self._root.getLeft().preorder_traversal() + \
                    self._root.getRight().preorder_traversal()

    # Processes the left subtree, then the node, then the 
    # right subtree
    # e.g.: the tree
    #     3
    #    / \
    #   1   5
    #  / \ / \
    # 0  2 4  6
    # would return [0 1 2 3 4 5 6]
    def inorder_traversal(self):
        return []

    # Processes the left subtree, the right subtree, and then
    # the node
    # e.g.: the tree
    #     6
    #    / \
    #   2   5
    #  / \ / \
    # 0  1 3  4
    # would return [0 1 2 3 4 5 6]
    def postorder_traversal(self):
        return []

# A few comments on traversals:
# * a "binary search tree" is one where all nodes in the left subtree
#   are less than or equal to the root, and all nodes in the right subtree
#   are greater than or equal to the root (and of course, the left and right
#   subtrees are also binary search trees)
# e.g:
#      5
#     / \
#    3   7
#   / \ / \
#  1  4 6  9
#  * a complete binary tree is one where every level is either full *or*
#    the last level's children are all "aligned to the left"
#  * a node's level is equal to the distance from that node to the root
#    (so the root's level is 0)
#  * the "height" of the tree is the "distance" between the root and the 
#    "lowest" child + 1
#    * suppose I have a height of x and it is a complete binary tree. How many
#      nodes are in the tree (give a range)?
#      * in a height of 3, I'd have at least 4 and at most 7 nodes
#      * in a height of 2, I'd have at least 2 and at most 3 nodes
#      * in a height of 4, I'd have at least 8 and at most 15 nodes
#      * in a height of x, I'd have at least 2^(x-1) and at most 2^x - 1
#  * searching a complete binary search tree is O(log n)

# For the weekend, think about how I might insert into a complete binary
# **search** tree and maintain the completeness property
# e.g. we want to avoid stuff like:
# 0
#  \
#   1
#    \
#     2
#      \
#       3
#        \
#         4
#         ...