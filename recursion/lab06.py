import math

path_cache = []

def cheapest_path_recursive_memoized(grid, x, y):
    if x == (len(grid) - 1) and y == (len(grid[0]) - 1):
        return (grid[-1][-1], '')
    elif x >= len(grid) or y >= len(grid[0]):
        return (math.inf, '')
    else:
        # If path_cache has a non-negative element at (x, y+1),
        # then right_move is equal to that; otherwise compute it
        # recursively and update the cache when finisheddown_move = cheapest_path_recursive_memoized(grid, x + 1, y)
        if y < len(grid[x]) - 1 and path_cache[x][y+1] == -1:
            path_cache[x][y+1] = cheapest_path_recursive_memoized(grid, x, y + 1)
            right_move = path_cache[x][y+1]
        else:
            right_move = (math.inf, '')
        
        if x < len(grid) - 1 and path_cache[x+1][y] == -1:
            path_cache[x+1][y] = cheapest_path_recursive_memoized(grid, x + 1, y)
            down_move = path_cache[x+1][y]
        

        # Only make this recursive call if the value at (x+1,y) is *not*
        # in path_cache ....
#        down_move = cheapest_path_recursive_memoized(grid, x + 1, y)

        if right_move[0] < down_move[0]:
            return (grid[x][y] + right_move[0], '')
        else:
            return (grid[x][y] + down_move[0], '')

def cheapest_path_memoized(grid):
    path_cache = [[-1] * len(grid[0]) for _ in grid]

    return cheapest_path_recursive_memoized(grid, 0, 0)

def fibonacci_naive(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_naive(n-1) + fibonacci_naive(n-2)

fib_cache = [0, 1] + [-1] * 100

def fibonacci_memoized(n):
    if fib_cache[n] == -1:
        fib_cache[n] = fibonacci_memoized(n-1) + fibonacci_memoized(n-2)

    return fib_cache[n]

if __name__=='__main__':
    print( cheapest_path_memoized([[1, 4,  2, 8],
                                   [2, 12, 1, 3],
                                   [5, 1,  1, 1]]) )
    print( cheapest_path([[1, 4,  2, 8],
                          [2, 12, 1, 3],
                          [5, 1,  1, 1]]) )

    print(fibonacci_memoized(100))
    print(fibonacci_naive(100))
