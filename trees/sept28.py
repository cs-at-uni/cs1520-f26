# Announcements:
# * Quiz 2 will be Wednesday and cover lists, stacks, queues, deques,
#   recursion. Sample problems include things like:
#   * using a data structure to solve a particular problem
#     * know the operations and overview of basic implementations
#     * you will **not** have to write your own data structure from class
#   * modifying a data structure to have some new property
#     * I will give you the superclass implementation
#     * note modifying a data structure could mean adding a new operation or
#       changing how an existing operation is performed
#   * solve a problem using recursion -- identify base case, recursive step,
#     etc.

# On Friday, we were talking about binary (search) trees! We talked about
# traversals (preorder, inorder, postorder). Note that if I have a binary
# search tree, I could perform an inorder traversal to get a sorted list
# of the elements of the tree.
#
# Suppose I have a binary search tree. What's the worst case running time
# for searching for an element? If the tree is unbalanced, this could be
# linear (O(n)). When should we rebalance a BST, and how should we rebalance
# a BST?
#
# When to rebalance:
# * periodically based upon a fixed time, # of inserts/deletes, etc.
# * when the "balance factor" is greater than x |height(right) - height(left)|
#   * as soon as x > 1, we have an unbalanced tree, but we don't necessarily
#     need to fix that right away
#
# How to rebalance:
# * (simple): 
#     (1) Get a list of nodes from an inorder traversal
#     (2) Set "center" node as the new root
#     (3) Balance left and right "sides" of list, setting result
#         as the left and right children of the root (respectively)
from sept25 import BinaryTreeNode
import collections

class BinarySearchTree():
    def __init__(self):
        self._root = None
        self._size = 0

    def insert(self, element):
        if self._root is None:
            self._root = BinaryTreeNode(element, None, None)
        elif self._root.getElement() >= element:
            self._root.getLeft().insert(element)
        else:
            self._root.getRight().insert(element)

    # The "iterator" design pattern involves an object that has two functions:
    # has_next() and next(). We'll implement an iterator for our 
    # BinarySearchTree class ... next week? Friday in a recorded lecture?
    def __iter__(self):
        return None

# A few samples for our main method

if __name__=='__main__':
    node1 = BinaryTreeNode(10, None, None)
    node2 = BinaryTreeNode(20, None, None)

    # We edited Sept. 25's Python a little to get this to work!
    if node1 > node2:
        print("OK")
    else:
        print("No")

    # OK, can I do a similar thing with the iterator for a data structure?
    # -- Yes! --
    # In fact, we expect collections to be iterable in Python!
    my_list = collections.deque() # [] () set() {}

    for element in my_list:
        print(element)

    tree = BinarySearchTree()

    for element in tree:
        print(element)

    '''
    # Build a binary search tree
    for value in range(10):
        tree.insert(value)

    # Iterate through all elements of a binary tree
    # ... but how can I get it to iterate over all elements
    # like this!?!?!??!?!?!?!
    for value in tree:
        print("Tree contains", value)
    '''