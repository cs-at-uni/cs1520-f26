# Graph Search! (from a starting node to a target)
# * Lab 10 introduced you to BFS (breadth-first search)
#   * BFS looks at all nodes at distance 1, then distance 2, then ... until the search
#     is successful
#     * this is what we'd want when we're looking for the shortest path
# * There is also depth-first search (DFS)
#   * This looks down one path, checking a node at distance 1, then 2, then 3, then 4, then ...
#   * frequently will find a path that isn't the shortest

## Implementing Graph Search
'''
Algorithm "graph search"(graph g, node start, node target):
1. Base case: is start == target, if so, exit with that path
2. visited = [start]
3. frontier = [start]
4. while frontier is not empty:
   * current node = frontier.remove()  &&& only difference between DFS and BFS &&&
   * if current is in visited: 
       continue
   * if current node == target node:
       return
   * visited.append( current )
   * frontier.append( neighbors of current )
5. Return false -- no path exists

Note: if we treat the frontier like a stack, we will be implementing DFS,
      while if we treat the frontier like a queue, we'll implement BFS 
'''