# Announcements:
# * No class on Friday
# * Any meetings for today will happen in 010 CEEE, *not* my office (015 H CEEE)

# Thanks for your patience and hard work on Lab 9. Any questions, feel free
# to reach out to me!

# Note we can certainly build a minheap with a linked data structure. This would
# be like the binary trees that we created earlier in the semester.

# We can, however, implement the minheap with an array-based list data structure!
class PriorityQueueHeap():
    def __init__(self):
        self._heap = [0]
        ...

    # Add the element to the end of the list and then "percolate up" the
    # element until it satisfies the min heap property again.
    def insert(self, k):
        self._heap.append(k)

        print(self._index_of_parent(len(self._heap) - 1))

        # We can look up the parent in the tree by using the index of this
        # last element. We'll "percolate" the value up until it's the 
        # smallest value in its subtree. This will require at most O(log n)
        # swaps!!
        ...

    # Remove the root and "percolate" a new root down the tree
    def delMin(self):
        ...
        return self._heap.pop(1)

    # Examples to figure out the formula to use: 
    # * 11 -> 5
    # * 5 -> 2
    # * 7 -> 3
    def _index_of_parent(self, child_index):
        return child_index // 2

# For more on minheaps, check out the textbook:
# * https://runestone.academy/ns/books/published/CS1520_UNI/Trees/BinaryHeapImplementation.html
# and Python's built-in `heapq` package:
# * https://docs.python.org/3/library/heapq.html

# Misc. comments on hash tables:
# * a way to store things with close-to-O(1) lookup using a hash function
# * would like to minimize the number of collisions of our hash function
# * the 'load factor' is the fraction of the table that is not empty

# Sample Quiz Questions:
# 1. Trace the "percolation" down the tree when deleting an element.
# 2. Give the time complexity of the various heap operations.