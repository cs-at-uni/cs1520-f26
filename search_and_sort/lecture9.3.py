# Quiz notes:
# I won't ask you to recreate a sorting algorithm. I might:
# * ask you which algorithm is given
# * ask you to informally describe an algorithm
# * ask for the worst-case running time for an algorithm
from random import randint, seed
from time import perf_counter_ns

# More sorting algorithms: merge sort
# Main idea: split the list into smaller sublists, sort those, and then
#            "merge" them back together.
# This is an O(n log n) sorting algorithm!
def mergeSort(alist):
    #print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)

# Final Sorting Algorithm: Quick Sort
# Quick sort works by organizing elements based upon a "pivot" element
# * after each "round", each element to the left of the pivot is less
#   than or equal to the pivot, and everything to the right of the pivot
#   is greater than or equal to.
# * fix the pivot element, "arrange" each side, repeat on the subproblems
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

if __name__=='__main__':
    seed(4)
    numbers = [randint(0, 10000) for _ in range(100000)]

    start_time = perf_counter_ns()
    #numbers.sort()
    #mergeSort(numbers)
    quickSort(numbers)
    end_time = perf_counter_ns()

    print('Total time:', (end_time - start_time))


# Running times:
# * Python's "sort": 16,194,098
# * Merge sort: 366,754,768
# * Quick sort: 225,375,537

# Note some sorts are "stable" (preserve the order of elements
# with equal keys in the original list)
# e.g. [('Berns', 3.2), ('Jimothy', 3.9), ('Fake', 3.9), ('Perfect', 4.0)]
# -- stable sorts will always have 'Jimothy''s tuple appear before 'Fake''s tuple
#    in the final result
#
# Apparently 3.11+ CPython implementations use "powersort":
# * https://en.wikipedia.org/wiki/Powersort