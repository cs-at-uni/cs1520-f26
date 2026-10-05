import sys

# Lecture 7.1
#
# Consider the recursive Fibonacci method:
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# The above method takes a long time for "larger" numbers
# like 50. This is because there is a lot of repeated computation.

# We can use a technique called 'memoization' to avoid repeated computation.
fibonacci_cache = [0, 1] + [-1]*100

def fibonacci_memoized(n):
    '''
    if fibonacci_cache[n] != -1:
        return fibonacci_cache[n]
    else:
        fibonacci_cache[n] = fibonacci_memoized(n-1) + fibonacci_memoized(n-2)
    '''
    if fibonacci_cache[n] == -1:
        fibonacci_cache[n] = fibonacci_memoized(n-1) + fibonacci_memoized(n-2)

    return fibonacci_cache[n]
    
if __name__=='__main__':
    print(fibonacci_memoized(int(sys.argv[1])))
    print(fibonacci(int(sys.argv[1])))