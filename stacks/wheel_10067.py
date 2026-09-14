'''
A poor solution to the 'Playing with Wheels' ICPC Problem #10067

The following lines are a sample input for your program.  It should complete in
only a few seconds after your two optimizations.  Mine ran in about 6 seconds
on an old 2.2 GHz i7.  The solution that should be returned is 8.

1
8 0 5 6
7 0 0 8
2
8 0 5 7
8 0 4 7
'''
import cProfile
import collections

def get_neighbors(state):
    neighbors = []
    state = list(state)
    for index, letter in enumerate(state):
        state[index] = str((int(letter) + 1) % 10)
        neighbors.append(''.join(state))
        state[index] = str(((int(letter) + 10) - 1) % 10)
        neighbors.append(''.join(state))
        state[index] = letter
    return neighbors


# Leaving this as its own function for reasons that will become apparent
# when examining the profiler's output ...
def not_in(element, collection):
    return element not in collection


def bfs(current, goal, forbiddens):
    frontier = collections.deque()#[]
    frontier.append((current, 0))
    visited = {}
    solved = False

    while len(frontier) > 0:
        state, steps = frontier.popleft()
        if state == goal:
            print(steps)
            solved = True
            break

        #visited.append(state)
        visited[state] = 1

        for neighbor in get_neighbors(state):
            if not_in(neighbor, visited):
                if neighbor not in forbiddens:
                    frontier.append((neighbor, steps + 1))

    if not solved:
        print(-1)


def main():
    cases = int(input())

    for _ in range(cases):
        current = ''.join(input().split())
        goal = ''.join(input().split())

        num_forbidden = int(input())
        forbiddens = []

        for _ in range(num_forbidden):
            forbiddens.append(''.join(input().split()))

        bfs(current, goal, forbiddens)


if __name__ == '__main__':
    cProfile.run('main()')
