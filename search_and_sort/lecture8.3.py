# Today's topic: searching (and maybe sorting)
# * a hash function is one that takes an arbitrarily-sized value and returns
#   a fixed size value (number)
import sys

def bad_hash(obj):
    return len(obj) % 20

if __name__=='__main__':
    name_1 = 'Andy Berns'
    name_2 = 'Olive Berns'

    #print(bad_hash(name_1))
    #print(bad_hash(name_2))

    roster = [None] * 21

    roster[bad_hash(name_1)] = name_1
    roster[bad_hash(name_2)] = name_2

    #print(roster)

    print(roster[bad_hash('George Washington')])

    # 'roster' is an example of a 'hash map': a map from keys to values
    # where the location is determined by the hash of the key
    roster_dict = {}

    # Hash maps give us O(1) lookups ("usually"), but there are a few
    # "gotchas"...:
    # * lots of wasted space to prevent "collisions" (two elements hash
    #   to the same value)
    # * collision resolution (how we deal with collisions) can add some overhead
    #   to the running time:
    #   * "open addressing" is where a value can be in some other spot than
    #     what is indicated by the key -- usually "linear probing"
    #     * linear probing inserts the value at the "next" open spot in the list
    #
    #   * "chaining": each spot in the map is a reference to a linked list of
    #                 values that hash to that spot

    # We can reduce the number of collisions by (i) making the hash table (list)
    # bigger (we want a low "load factor"), or (ii) making a better hash function
    # (a "perfect" hash function is one that hashes each unique object to a
    #  unique value)
    
    name_3 = 'Irie Berns'
    roster[bad_hash(name_3)] = name_3

    print(roster)

    print(sys.getsizeof([1]))
    print(sys.getsizeof({'1': 1}))

    # A map ADT has the following operations:
    # * get( key )
    # * put( key, value )
    # * delete( key )
    # * size( )
    # * keys( )
    #
    # Note that a 'map' doesn't necessarily have to use hashing, it just needs
    # to correlate keys to values

    # Topic 2: Sorting
    # (we'll know how they work, but we hopefully never have to write one ourselves)
    #
    # The classic "first sort" to see is _bubble sort_...
    # * check 0 v 1, 1 v 2, 2 v 3, etc.
    # * larger values "bubble up" to the top -- each iteration brings the largest
    #   element in the unsorted portion to the "top" of the unsorted portion
    #   * [9 7 5 3] ==> after 1 iteration, 9 is at the last position
    # * performance: n-1 comparisons + n-2 comparisons + ... + 3 comparisons + ...
    #   ==> O(n) comparisons each time through, O(n) times through
    #       ==> O(n^2) comparisons each time with bubble sort (worst case)
    # * could stop early if no swaps were made in a pass, resulting in O(n)
    #   (for cases when the list is already sorted)