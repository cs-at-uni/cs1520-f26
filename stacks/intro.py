# I will bring a few printed copies of lecture notes, and try
# and do a better job of posting them in advance.

# "Abstract data types" (ADTs): a definition of a set of operations
# we can perform on a data type (and legal values of that type).
# -- note this doesn't talk about implementation --

# Lists (in Python): Operations
# * accessing an element (my_list[i])
# * adding an element to the end (my_list.append(elem))
# * removing an element (my_list.remove(elem))
# * ... see Lec. 3 handout ...

# List Implementation in Python
# * the default list implementation in Python uses __arrays__
# * I could still implement the "list ADT" from Lecture 3's notes
#   without using arrays: I could use a _linked list_.

# Lists as Arrays:
# * start with a fixed size, when you exceed the size allocated
#   you allocate new space and copy all the elements over
#   * in the worst case, an insertion (at the end) could be an O(n) 
#     operation
#     * the "amortized cost" (or cost spread over time) is O(1)
# * Inserting an element at the front is O(n) all the time

# A singly-linked list node
class SinglyLLNode(object):
    def __init__(self, element, next):
        self._data = element
        self._reference_to_next = next


# A singly-linked list
class SinglyLinkedList(object):
    def __init__(self, element):
        self._head = SinglyLLNode(element, None)

    def append(self, element):
        # Skip over all LLNodes until you reach "the end"
        cursor = self._head

        while cursor._reference_to_next != None:
            cursor = cursor._reference_to_next
        
        # Create a new node and make the last old node point to it
        new_node = SinglyLLNode(element, None)
        cursor._reference_to_next = new_node

    def get(self, index):
        cursor = self._head

        while index > 0:
            cursor = cursor._reference_to_next
            index = index - 1

        return cursor._data


class DoublyLLNode(object):
    def __init__(self, element, next, prev):
        # Try to implement this before the next class (Friday)
        pass


if __name__=='__main__':
    my_list = SinglyLinkedList(10)
    my_list.append(20)
    my_list.append(30)
    print(my_list.get(2))