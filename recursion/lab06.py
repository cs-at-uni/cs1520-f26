import math

def cheapest_path_recursive(map, x, y):
    if x == (len(map) - 1) and y == (len(map[0]) - 1):
        return (map[-1][-1], '')
    elif x >= len(map) or y >= len(map[0]):
        return (math.inf, '')
    else:
        right_move = cheapest_path_recursive(map, x, y + 1)
        down_move = cheapest_path_recursive(map, x + 1, y)

        if right_move[0] < down_move[0]:
            return (map[x][y] + right_move[0], '')
        else:
            return (map[x][y] + down_move[0], '')

def cheapest_path(map):
    return cheapest_path_recursive(map, 0, 0)

if __name__=='__main__':
    print( cheapest_path([[1, 3, 4, 5],
                          [1, 3, 100, 2],
                          [9, 8, 100, 4]]) )