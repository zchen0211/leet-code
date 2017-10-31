"""
323. Number of Connected Components in an Undirected Graph (Medium)

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""

class Solution(object):
  def countComponents(self, n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: int
    """
    par_map = [-1] * n
    if n == 0: return 0

    for edge in edges:
      i, j = edge
      # par of i
      par_i = i
      while par_map[par_i] != -1:
        par_i = par_map[par_i]

      # par of j
      par_j = j
      while par_map[par_j] != -1:
        par_j = par_map[par_j]

      if par_i != par_j:
        par_i, par_j = min(par_i, par_j), max(par_i, par_j)
        par_map[par_j] = par_i
    return par_map.count(-1)


if __name__ == "__main__":
  a = Solution()
  print a.countComponents(5, [[0, 1], [1, 2], [3, 4]])

