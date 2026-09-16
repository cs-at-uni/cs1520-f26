# Stack ADT:
# * push(element): adds 'element' to the top of the stack
# * pop(): removes and returns the element at the top of the stack
# * size(): returns the number of elements in the stack
# * peek(): returns the top element of the stack (like a pop and push)

# A stack is a LIFO (last in, first out) data structure

class ListStack(object):
    def __init__(self):
        self._stack = []
    
    # push is O(1) on average/"amortized analysis"
    def push(self, element):
        self._stack.append(element)
    
    # pop is O(1)
    def pop(self):
        return self._stack.pop()
    
    def size(self):
        return len(self._stack)

class LinkedNode():
    def __init__(self, element, next):
        self._element = element
        self._next = next

class LinkedStack(object):
    def __init__(self):
        self._head = None
        self._size = 0

    # Note I don't check, increment, or decrement size ... can you add that?
    def pop(self):
        element = self._head._element
        self._head = self._head._next
        return element

    def push(self, element):
        self._head = LinkedNode(element, self._head)

# .......

# When would we use stacks?
# * fun uses on leetcode.com
# * matching brackets/parentheses/delimiters...
#   *e.g. determine if a given string of open and close brackets ([])
#         is "balanced" (each open followed by a corresponding close)
#         - [[[]][][]][] is balanced
#         - ][ is not balanced
def is_balanced_string(input_string):
    openers = ListStack()

    for character in input_string:
        if character == '[':
            openers.push('[')
        else:
            openers.pop()
    
    return openers.size() == 0

if __name__=='__main__':
    print(is_balanced_string(input()))

    a_stack = LinkedStack()
    a_stack.push(10)
    a_stack.pop()
    a_stack.pop()

# For 9/15's lab, we will hopefully 
# (a) read a problem description,
# (b) choose the right data structure for solving it, and then
# (c) actually solve it.