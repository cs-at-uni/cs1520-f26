# Recursion:
# * Write a recursive function to compute the n-th Fibonacci
#   number [ F(n) = F(n-1) + F(n-2), F(0) = 0, F(1) = 1 ]
def fibonacci(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Now that we understand recursion, we can start working with
# some data structures whose definition is naturally recursive.
# In particular, we can start looking at _trees_!!
#
# A binary tree is either None *or* consists of three elements:
# (i) A root node (usually holding a value)
# (ii) A 'left child', which is a binary tree
# (iii) A 'right child', which is a binary tree
#
#        5
#       / \
#      2   7
#     / \ / \
#    1  3 6  8
#
# * 5 is the "root" of the tree
# * 1, 3, 6, and 8 are "leaves"
# * 5, 2 and 7 are "internal" nodes (our term) -- nodes with at
#   least one (non-None) child
# (note the "special" property of this tree above: everything
#  in the left subtree is less than the root, everything in the
#  right subtree is greater than the root)

# Implement a binary tree data structure, starting with the 
# BinaryTreeNode class.
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

class BinaryTree():
    def __init__(self):
        self._root = None

if __name__=='__main__':
    print(fibonacci(5))