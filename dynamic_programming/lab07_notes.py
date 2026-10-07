import unittest

def schedule_dynamic(available_jobs):
    results = [-1] * len(available_jobs)

    results[-1] = available_jobs[-1]
    results[-2] = max(available_jobs[-1], available_jobs[-2])

    for index in range(len(available_jobs) - 3, -1, -1):
        results[index] = max(results[index + 1], available_jobs[index] + results[index + 2])

    return results[0]



schedule_cache = []

def schedule_memoized(available_jobs, starting_index):
    global schedule_cache
    if len(schedule_cache) == 0:
        schedule_cache = [-1] * (len(available_jobs) + 2)

    if starting_index == len(available_jobs):
        return 0
    elif starting_index == len(available_jobs) - 1:
        return available_jobs[-1]
    else:
        if schedule_cache[starting_index + 2] == -1:
            schedule_cache[starting_index + 2] = schedule_memoized(available_jobs, starting_index + 2)

        if schedule_cache[starting_index + 1] == -1:
            schedule_cache[starting_index + 1] = schedule_memoized(available_jobs, starting_index + 1)

        return max(available_jobs[starting_index] + schedule_cache[starting_index + 2],
                   schedule_cache[starting_index + 1])

def schedule_trucking_jobs(available_jobs):
    # available_jobs is a list of values for taking the job at index i
    #
    # schedule_trucking_jobs returns the maximum value I could achieve
    # from the given list of available jobs (for now)
    pass
    # Base Cases:
    if len(available_jobs) == 0:
        return 0
    elif len(available_jobs) == 1:
        return available_jobs[0]

    # Recursive Step:
    else:
        # return whatever is larger: the best return I can get from _not_ scheduling
        #                            today, (best value of [1:]) or the best return I can 
        #                            get from scheduling today (today's value [0] + best value of [2:])
        return max(available_jobs[0] + schedule_trucking_jobs(available_jobs[2:]),
                   schedule_trucking_jobs(available_jobs[1:]))

class TruckSchedulingTest(unittest.TestCase):
    def test_few_jobs(self):
        self.assertEqual(schedule_trucking_jobs([1,50,100,3]), 101)
        self.assertEqual(schedule_trucking_jobs([50,1,100,4]), 150)
        self.assertEqual(schedule_dynamic([3, 2, 10, 5, 5, 20]), 33)

    def test_many_jobs(self):
        self.assertEqual(schedule_trucking_jobs([1]*36), 18)
        self.assertEqual(schedule_memoized([1]*100, 0), 50)
        self.assertEqual(schedule_dynamic([1]*200), 100)

if __name__=='__main__':
    unittest.main()