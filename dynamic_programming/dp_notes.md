# Lecture 7.3
Today we'll practice identifying subproblems in dynamic programming problems. We'll take all of our problems from https://leetcode.com/problem-list/dynamic-programming/.

If you'd like, you can post your solution as a reply to a discussion post on Blackboard I'll make later today.

## 70: Climbing Stairs
* What are some base cases?
  * 0 steps has 1 way to climb
  * 1 step has 1 way to climb
  * 2 steps has 2 ways to climb (1+1, 2)
* What about the "next" number, such as 3?
  * 3 steps has 3 ways to climb (1+1+1, 1+2, 2+1)
* Can we describe the solution for 4 in terms of subproblems?

## 118: Pascal's Triangle
## 119: Pascal's Triangle II
## 121: Best Time to Buy and Sell Stock
* "Base cases":
  * [1, 2] has a profit of 1
  * [2, 1] has no profit (0)
* Can we describe the solution in terms of subproblem solutions?

## 338: Counting Bits
* What are some "base cases"?
  * 0 has 0 `1`s, 1 has 1 `1`
* What about the "next" number?
  * 2 has 1 `1`, 3 has 2 `1`s, 4 has 1 `1`s, 
* Can we describe the solution for 3 with the solutions to other subproblems?
  * still an open problem ...

## 392: Is Subsequence
* "Base cases":
  * "ac" is a subsequence of "abc"
  * "ac" is not a subsequence of "cba"
  * "a" is a subsequence of "jkdasiogeid"
* Can we describe the solution in terms of solutions to smaller subproblems?

## 746: Min Cost Climbing Stairs
## 1025: Divisor Game
## 1137: N-th Tribonacci Number
## 1668: Maximum Repeating Substring
* What are some "base cases"?
  * "ab" appears in "bcacb" 0 times
  * "ab" appears in "ab" 1 time
* What about "ab" in "abababc"?
  * answer is 3
* Can we describe the solution for "ab","abababc" in terms of solutions to other subproblems?