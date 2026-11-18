'''
Announcements:
* 2 lab sessions left -- only one of those (December 1) will involve a new lab
  * last week's session will be open "office hours"
* December 9 (last Wednesday of the semester) will be our last quiz
  * this will mainly cover graphs: given a problem description, state what the graph
    would be and what graph algorithm you'd use (or problem you'd solve)
* 2 assignments are coming...
  * 1 of those is from Dr. Fienup and will be posted today
  * 1 of these will be from me! (cuckoo hashing -- show up to class and this should be
                                 easy ...)
* turn in your AVL tree worksheet for quiz "5" credit
'''

'''
Some basic graph definitions from CS 1800:
* degree of node u: the number of edges incident on (connected to) node u
* clique of n nodes: completely-connected component of n nodes
  * each node would have a degree of (n - 1)
* path between nodes u and v: ordered sequence of edges (u, w_1), (w_1, w_2), ...,
  (w_n, v) (a way to step from u to v)
  * this is a path of length n + 1
  * the _shortest path_ is the smallest sequence of edges from u to v
* a directed graph may be _cyclic_ or _acyclic_
  * a directed acyclic graph (DAG) is one where there is no path from any node u
    back to node u (no "cycles")

Some graph problems we might want to solve (beyond the searches and sorts we've seen
so far) include:
* Graph Coloring: assign labels ("colors") to nodes in a graph such that no two 
                  neighbors have the same label ("color")
  * the goal here is to use as few colors as possible
* Maximum Independent Set: select the largest set of nodes such that no two nodes
                           in the set has a neighbor also in the set (aka all nodes
                           are "independent")
  * the goal here is to maximize (duh) the size of the independent set
'''

'''
Solving problems with graphs: 
1. Exercise 3.7 (Kleinberg and Tardos): Let's suppose that the claim is not true. That
   is, we have a graph of n nodes (n is even), every node has a degree at least n/2, 
   but G is _not_ connected.
   * Since G is not connected, there are at least two connected components.
   * Let S be the smallest connected component from our graph G. This has a size
     of _at most_ n/2
   * What's the maximum degree of a node in S? n/2 - 1
     * CONTRADICTION: we assumed every node in G has a degree of at least n/2, but
                      this is impossible if we have a connected component of size at
                      most n/2.

2. Exercise 3.11 (Kleinberg and Tardos): the book says you should find a solution
   that is O(m + n), where m is the number of edges and n is the number of nodes.
   * check out the solution at https://github.com/mathiasuy/Soluciones-Klenberg/tree/master/chapter_03
     -- if you bring in a _handwritten_ answer in your own words for the next quiz,
        I'll give you bonus quiz points
'''