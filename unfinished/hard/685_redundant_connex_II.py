"""
685. Redundant Connection II (Hard)

In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v, where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3

Example 2:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.
"""

class Solution(object):
  def findRedundantDirectedConnection(self, edges):
    """
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    par_map = {}
    node2 = None
    node2_par = None
    root_set = set()
    loop = False
    loop_set = set()
    for item in edges:
      i, j = item
      # potential root
      if i not in par_map:
        root_set.add(i)
      if j in par_map and j in root_set:
        root_set.remove(j)
      # check loop conflict, return loop case
      tmp_par = i
      while tmp_par in par_map:
        tmp_par = par_map[tmp_par]
        if tmp_par == j: # conflict
          loop = True
          break
      if loop and len(loop_set) == 0:
        

      if j not in par_map:
        par_map[j] = i
      else:
        node2 = j
        node2_par = (par_map[j] , i)
      print par_map

    print 'in-degree: 2', node2
    print root_set
    if len(root_set) == 0:
      return node2_par[1]

if __name__ == "__main__":
  a = Solution()
  print a.findRedundantDirectedConnection([[1,2], [1,3], [2,3]])
  print a.findRedundantDirectedConnection([[1,2], [2,3], [3,4], [4,1], [1,5]])
  print a.findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]])
