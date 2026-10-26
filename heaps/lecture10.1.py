# Priority Queue: the element with the "highest priority" (usually
#                 smallest number) is returned first.
# * delMin(): removes and returns the highest priority item
# * insert(k): insert an element with priority k into the queue
# * size(): returns the number of elements in the queue
# * ... (book has a few more operations)

# An easy implementation: a list of elements
class PriorityQueueList():
    def __init__(self):
        self._elements = []

    # O(n) complexity (O(n) for min, O(n) for index, O(n) for pop ==
    #                  O(3n) = O(n))
    def delMin(self):
        min_value = min(self._elements)
        min_position = self._elements.index(min_value)
        return self._elements.pop(min_position)

    # O(1) complexity
    def insert(self, element):
        self._elements.append(element)

    # O(1) complexity
    def size(self):
        return len(self._elements)

# Our simple implementation is not very "efficient": it is linear in the number
# of elements in the queue. Could we use a binary tree data structure to
# more-effectively store and retrieve the data?
#
# Yes! We can use a binary tree organized into what we call a "min heap"
#      (or min-heap or minheap). A min heap is a **complete** binary tree where
#      every element in a subtree is greater than the parent element.
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

# Sample Quiz Questions:
# 1. Is the given tree a heap? (aka is it complete and satisfying the min
#    heap property?)
# 2. Draw a complete binary tree/define a complete binary tree.
# 3. Define or draw a min heap.
# 4. Trace a "percolation" up the heap on an insertion, drawing each step
#    until the heap property is restored.