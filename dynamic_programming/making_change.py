# Memoization avoids repeated computation. It's kind of a "top down"
# method -- it starts by asking to compute the "final" answer and builds
# this up from there.
#
# This is similar to a technique called "dynamic programming" -- the
# main difference is that this builds "bottom up".
#
# The classic problem for this is the change making problem. Suppose
# you need to get a collection of coins that equal 25. What coins
# should you use to make this in the fewest number of coins?
# First, how many coins would we need?
# * in the US, we can use a simply greedy algorithm
#   * e.g. 27 would take a 25, 1, 1 ==> 3 coins
#
# What if we had 1, 5, 10, 21, and 25? How many coins would I need
# to make 63 units? A greedy algorithm would say 25 + 25 + 10 + 1 + 1 + 1 ==> 6
# __but__ the real answer is 3: 21 + 21 + 21. We can try every combination
# then to make sure we're getting the best one
#
# Note we have lots of "overlapping subproblems" here (aka repeated
# computation) and we have "optimal substructure" (basically an optimal answer
# doesn't depend upon how you got to that point). **It might be an interesting
# quiz question to ask which of three problems look amenable to dynamic
# programing or memoization...**
#
# [0, 1, 2, 3, 4, 1, ...] could be the start of a lookup table: what's the
# minimum number of coins required to make n?
# e.g. # of coins to make 6 = min( 1 + # of coins to make 5,
#                                  1 + # of coins to make 1,
#                                  ----- (all else are impossible))
#                         6 = 1 + min( # to make 5, # to make 1)
#
# Can you think of a general form for this?
# to make x, I need 1 + min( # to make (x - 25), # to make (x - 21),
#                            # to make (x - 10), # to make (x - 5),
#                            # to make (x - 1))
#
# Another example: min_coins(denoms = [1, 7, 10], value = 15)
# [0, 1, 2, 3, 4, 5, 6, 1, 2, 3, 1, ...]
#
#                                  {# of coins to make (x-1)
#   # of coins to make x = 1 + min {# of coins to make (x-7)
#                                  {# of coins to make (x-10)