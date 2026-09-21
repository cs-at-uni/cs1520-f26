import unittest

def sum_list(num_list):
    if len(num_list) == 0:
        return 0
    else:
        return num_list[0] + sum_list(num_list[1:])

def factorial(n):
    # Base Case: n = 0
    if n == 0:
        return 1
    else:
        # Recursive step
        return n * factorial(n-1)

# Base case: what's a simple case where I already know the answer?
# Recursive step: what's the least amount of work I have to do to build the answer
#                 from a smaller version?

class RecursionTester(unittest.TestCase):
    def testSumList(self):
        self.assertEqual(15, sum_list([1,2,3,4,5]))

    def testFactorial(self):
        self.assertEqual(6, factorial(3))
        self.assertEqual(120, factorial(5))

if __name__=='__main__':
    unittest.main()