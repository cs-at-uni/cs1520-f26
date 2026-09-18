# Queues are FIFO data structures (first in, first out)
# Major operations (besides the standard size, __repr__, etc.):
# * enqueue(element)
# * dequeue() --> element

# If you get a chance to study before Friday, go ahead and see if you can write
# a queue using either an array or a linked list (or both!)

# On Friday, we'll do an activity much like the Lab 4 activity, only with queues
# instead of stacks

class StacksQueue():
    def __init__(self):
        self._main_stack = []

    def enqueue(self, element):
        self._main_stack.append(element)

    def dequeue(self):
        # Put everything from _main_stack to temp_stack
        temp_stack = []

        while(len(self._main_stack) > 0):
            temp_stack.append(self._main_stack.pop())

        element = temp_stack.pop()

        while(len(temp_stack) > 0):
            self._main_stack.append(temp_stack.pop())
        
        return element
    
    def size(self):
        return len(self._main_stack)
    
    def is_empty(self):
        return self.size() == 0

if __name__=='__main__':
    my_queue = StacksQueue()

    for num in range(10):
        my_queue.enqueue(num)

    for _ in range(10):
        print(my_queue.dequeue())