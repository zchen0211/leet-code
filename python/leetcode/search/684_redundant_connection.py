"""
684. Redundant Connection (Medium)

We are given a "tree" in the form of a 2D-array, with distinct values for each node.

In the given 2D-array, each element pair [u, v] represents that v is a child of u in the tree.

We can remove exactly one redundant pair in this "tree" to make the result a (rooted) tree.

You need to find and output such a pair. If there are multiple answers for this question, output the one appearing last in the 2D-array. There is always at least one answer.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: Original tree will be like this:
  1
 / \
2 - 3

Example 2:
Input: [[1,2], [1,3], [3,1]]
Output: [3,1]
Explanation: Original tree will be like this:
  1
 / \\
2   3
Note:
The size of the input 2D-array will be between 1 and 1000.
Every integer represented in the 2D-array will be between 1 and 2000.
"""

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Union Find:
        # Notice the merging part should be on parent level
        par_map = {}
        for edge in edges:
            print par_map
            i, j = min(edge), max(edge)
            if i == j: return edge
            # check if connected?
            par_i = i
            while par_i in par_map:
                par_i = par_map[par_i]
            par_j = j
            while par_j in par_map:
                par_j = par_map[par_j]
            if par_i == par_j:
                return edge
            else:
                par_i, par_j = min(par_i, par_j), max(par_i, par_j)
                par_map[par_i] = par_j
            print par_map


if __name__ == "__main__":
    a = Solution()
    # print a.findRedundantConnection([[1,2], [1,3], [2,3]])
    # print a.findRedundantConnection([[1,2], [1,3], [3,1]])
    print a.findRedundantConnection([[2,3],[5,2],[1,5],[4,2],[4,1]])
