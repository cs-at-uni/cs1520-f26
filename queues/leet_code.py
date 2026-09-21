# Problem 1700(variant): number of Irie's friends unable to eat

# We can simulate this, but do we have to? I think so, because:
# ... can we come up with a counter example where (a) there are k
# friends and (b) k sandwiches equal to the k friends, but there
# are unfed friends?
#
# Attempt 1: [1 0 1 0] friends, [0 1 0 1] sandwiches
# Attempt 2: [1 1] friends, [0 1] sandwiches ==> 2 friends go hungry
# ... it seems like this can be computed without simulation, but
#     let's simulate it for fun!
import unittest

def feeding_friends(friends, sandwiches):
    passes_left = len(friends)

    while(len(friends) > 0 and passes_left > 0):
        friend = friends.pop(0)

        if friend == sandwiches[-1]:
            sandwiches.pop()
            passes_left = len(friends)
        else:
            friends.append(friend)
            passes_left = passes_left - 1

    return len(friends)

# Friends       Sandwiches     Result
# ===================================
#  [1 1]         [0 0]           2
#  [0 0]         [0 0]           0

class FeedingFriendsTester(unittest.TestCase):
    def test_all_eat(self):
        self.assertEqual(feeding_friends([1,1], [0,0]), 2)

if __name__=='__main__':
    unittest.main()