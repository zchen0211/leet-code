'''
310. Minimum Height Trees (Medium)

For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]

Show Hint 
Note:

(1) According to the definition of tree on Wikipedia: "a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree."
(2) The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
'''

class Solution(object):
  def findMinHeightTrees(self, n, edges):
    if n == 0: return []
    edge_dict = {}
    for i, j in edges:
      if i in edge_dict: edge_dict[i].append(j)
      else: edge_dict[i] = [j]
      if j in edge_dict: edge_dict[j].append(i)
      else: edge_dict[j] = [i]
    print edge_dict

    res_dic = {}
    for i in range(n):
      # calculate depth
      stack1 = [i]
      stack2 = []
      visited = set([])
      depth = 0
      # bfs and increase depth
      while(stack1):
        while(stack1):
          j = stack1.pop()
          visited.add(j)
          for k in edge_dict[j]:
            if k not in visited:
              stack2.append(k)
        depth += 1
        stack1, stack2 = stack2, stack1
      print i, depth
      res_dic[i] = depth
    min_depth = min(res_dic.values())
    result = []
    for k in res_dic.keys():
      if res_dic[k] == min_depth:
        result.append(k)
    return result
  # over-time

  def findMinHeightTrees2(self, n, edges):
    if n == 0: return []
    if n == 1: return [0]
    edge_set_list = []
    # keep all the edges
    for i in range(n):
      edge_set_list.append(set([]))

    # add all edges into the set
    for i, j in edges:
      edge_set_list[i].add(j)
      edge_set_list[j].add(i)
    leaves = [item for item in range(n) if len(edge_set_list[item])==1]
    print edge_set_list
    print leaves    
    # check and remove all nodes with 1 in-degree
    result = range(0, n)
    while(len(leaves)!=n):
      # remove leaves
      new_leaves = []
      n -= len(leaves)
      for i in leaves:
        j = edge_set_list[i].pop()
        edge_set_list[j].remove(i)
        if len(edge_set_list[j]) == 1: new_leaves.append(j)
      # update edge_set_list
      leaves = new_leaves
    return leaves

if __name__ == '__main__':
  a = Solution()
  print a.findMinHeightTrees2(1, [0])
  # print a.findMinHeightTrees2(4, [[1, 0], [1, 2], [1, 3]])
  # print a.findMinHeightTrees2(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])
