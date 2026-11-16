'''
Announcements:
* no lab tomorrow (11/17)
* three weeks of lectures left

(Directed) Graph representations!
* linked graph (Node objects, each with a "_neighbors" list variable)
* adjacency matrix (a list of lists, each containing a non-zero value where an edge exists)

(1) --> (2) --> (3)
        (2) --> (4)

Linked: Node(id = 1, _neighbors = [Node(2)])
        Node(id = 2, _neighbors = [Node(3), Node(4)])
        Node(id = 3, _neigbhors = [])
        Node(id = 4, _neighbors = [])

Adjacency matrix:
[ [0 1 0 0]
  [0 0 1 1]
  [0 0 0 0]
  [0 0 0 0] ]

When might a linked representation be better?
* less space required on sparse graphs

When might an adjacency matrix be better?
* less space required on dense graphs
'''

'''
Exercises for Chapter 3 of "Algorithm Design"
* the hard part of CS is transforming a "real" problem into a graph problem
  -- once you know it's a graph, you can use existing tools to solve your
  "real" problem

Example: I want to register for classes. I know for sure I'd like to take
         CS 4740 (Real-Time Embedded Systems) as soon as possible. What courses
         should I take this semester?
         * Nodes == n courses
         * Edges == m prereqs (A --> B iff A is a prereq of B)
         * Solution: topological sort

Exercise 3.4: What are the nodes and edges, and what am I doing with them?
* Nodes == specimens
* Edges == judgements -- each with a label of "same" or "different"

Suppose two butterflies x and y are labeled "same". I want to make sure both x/y are 
**not** labeled same/different to some other butterfly z.
* every butterfly that x is the "same" as does not have a "different" edge to y

Some solution hints:
* https://github.com/mathiasuy/Soluciones-Klenberg/tree/master/chapter_03

We have one quiz remaining. I will give you 1-3 problem descriptions and ask you
to convert the real problem into a graph problem.
'''