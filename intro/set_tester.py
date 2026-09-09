import time
import sys

# Abstract Data Type (ADT) for 'set':
# * insert(elem)    -- adds 'elem' to the set
# * contains(elem)  -- returns True when 'elem' is in the set
# * remove(elem)    -- removes 'elem' from the set

'''
How could you implement your own set in Python?
1) With a list:
   * insert(elem): append elem to the list
   * contains(elem): return True exactly when list contains elem
   * remove(elem): scan through list, removing each occurrence of elem

2) With a dictionary:
    * insert(elem): set dictionary[elem] = 1
    * contains(elem): check elem in dictionary
    * remove(elem): dictionary.pop(elem) 
'''

'''
Evaluating implementations of ADTs:
* Time Complexity
* Space Complexity
'''

if __name__=='__main__':
    set_list = [0 for _ in range(int(sys.argv[1]))]

    start_time = time.perf_counter_ns()

    # Perform an operation
    for _ in set_list:
        pass

    end_time = time.perf_counter_ns()

    print('Total time:', end_time - start_time)