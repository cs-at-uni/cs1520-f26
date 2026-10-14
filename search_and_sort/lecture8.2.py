# Quiz Review
# 1. Write a recursive function to solve problem with overlapping subproblems.
# 2. Memoize a given recursive solution to a problem above.
# 3. Given a problem description, write the solution in terms of the
#    subproblem(s).
# 4. Write a {pre,in,post}-order traversal for a binary tree.
# 5. What order would the nodes be "processed" in a {pre,in,post}-order
#    traversal for the given tree.

# Iterator/Iterable
# * in Python, an object is Iterable if you can ask it to return an iterator
#   using the __iter__ function.
#   * if a colletion is Iterable in Python, I can use a for loop to process
#     all of the elements in the collection
#
# * an Iterator is capable of returning a reference to the "next" element
#   in the collection in response to the __next__ function
#   * if an Iterator is asked for its next element and there is not one,
#     it should raise a StopIteration exception

class SinglyLinkedNode(object):
    def __init__(self, element, next):
        self._data = element
        self._reference_to_next = next


# A singly-linked list
class SinglyLinkedList(object):
    def __init__(self, element):
        self._head = SinglyLinkedNode(element, None)

    def append(self, element):
        # Skip over all LLNodes until you reach "the end"
        cursor = self._head

        while cursor._reference_to_next != None:
            cursor = cursor._reference_to_next
        
        # Create a new node and make the last old node point to it
        new_node = SinglyLinkedNode(element, None)
        cursor._reference_to_next = new_node

    def get(self, index):
        cursor = self._head

        while index > 0:
            cursor = cursor._reference_to_next
            index = index - 1

        return cursor._data

    def __iter__(self):
        return LinkedListIterator(self._head)


# Let's make an iterator for a singly-linked list
# (we need a "next" function)
class LinkedListIterator():
    def __init__(self, cursor):
        self._cursor = cursor

    def __next__(self):
        if self._cursor is None:
            raise StopIteration
        
        next_element = self._cursor._data
        self._cursor = self._cursor._reference_to_next

        return next_element
    
if __name__=='__main__':
    '''
    my_list = [1, 2, 4, 5]

    for number in my_list:
        print(number)
    '''

    my_iterable_list = SinglyLinkedList(5)
    my_iterable_list.append(1)
    my_iterable_list.append(2)

    for number in my_iterable_list:
        print(number)

# I could use iterators anywhere I have a collection of elements:
# for instance, I could have a tree with an in-order iterator that goes
# through the elements in an in-order traversal. You can try to write
# this for fun (or I can write it and send it).
#
# Caveat: the way I've done it above is totally not the Pythonic way to
#         do it ...