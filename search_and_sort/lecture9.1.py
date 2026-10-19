# Quiz 3 is now Wednesday, October 21
# * Feel free to contact me with any questions!!!!!

# General note: the sum of the first n positive integers is [n(n+1) / 2]
#
# Sorting Algorithms!!
# * Bubble Sort -- large values "bubble up" to the top
# * Selection Sort -- we "select" the largest/smallest value and move it to the
#                     end of the unsorted portion (book uses largest to help 
#                     differentiate from insertion sort)
#                     Worst-case running time: O(n^2)
#                     (best case is O(n^2))
# From the book:
def selection_sort(number_list):
   for fill_slot in range(len(number_list)-1,0,-1):
       position_of_max=0
       for location in range(1,fill_slot+1):
           if number_list[location]>number_list[position_of_max]:
               position_of_max = location

       temp = number_list[fill_slot]
       number_list[fill_slot] = number_list[position_of_max]
       number_list[position_of_max] = temp

# * Insertion Sort -- find the next element and "insert" it into the sorted
#                     portion of the list
#                     Worst case running time: O(n^2)
#                     (best case is O(n))
# From the book:
def insertion_sort(number_list):
   for index in range(1,len(number_list)):

     current_value = number_list[index]
     position = index

     while position > 0 and number_list[position-1] > current_value:
         number_list[position]=number_list[position-1]
         position = position-1

     number_list[position]=current_value

# Quiz Check In: 
# * Could you describe each sort in a single sentence?
# * Give me the worst-case running time of each sorting algorithm.
# * Give me a configuration which realizes this worst-case behavior.
# * Give me a configuration which realizes the _best case_ behavior.

# * Shell sort: sorts sublists and then sorts resulting list, named after
#               inventor Donald Shell
#   (like insertion sort only keeps it to a bounded number of shifts that
#    you have to do)
#
# After the first pass, what can I say about a number that is supposed to be
# in the "first half" after everything is sorted?
def shell_sort(number_list):
    sublist_count = len(number_list)//2
    while sublist_count > 0:

      for start_position in range(sublist_count):
        gap_insertion_sort(number_list,start_position,sublist_count)

      print("After increments of size",sublist_count,
                                   "The list is",number_list)

      sublist_count = sublist_count // 2

def gap_insertion_sort(number_list,start,gap):
    for i in range(start+gap,len(number_list),gap):

        current_value = number_list[i]
        position = i

        while position >= gap and number_list[position-gap] > current_value:
            number_list[position]=number_list[position-gap]
            position = position-gap

        number_list[position]=current_value