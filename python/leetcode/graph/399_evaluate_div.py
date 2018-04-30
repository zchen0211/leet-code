"""
399. Evaluate Division (Medium)

Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0. 
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""

class Solution(object):
  def calcEquation(self, equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    # record results
    node_set = set()
    edge_dict = {}
    n = len(equations)

    for i in range(n):
      num, den = equations[i]
      val = values[i]
     
      if num not in edge_dict:
        edge_dict[num] = {den: val, num: 1.}
      else:
        edge_dict[num][den] = val

      if den not in edge_dict:
        edge_dict[den] = {num:1./val, den: 1.}
      else:
        edge_dict[den][num] = 1./val
    print edge_dict

    result = []
    # tackle queries
    for item in queries:
      num, den = item
      if num not in edge_dict or den not in edge_dict:
        result.append(-1.)
      elif num in edge_dict and num == den:
        result.append(1.)
      else: # traverse graph
        val = self.traverse(num, den, edge_dict)
        result.append(val)
    return result

  def traverse(self, start, end, edge_dict):
    visited = {start: 1.}
    stack = [start]
    # dfs
    while(stack):
      node = stack.pop()
      curr_val = visited[node]
      for k in edge_dict[node]:
        if k not in visited:
          visited[k] = edge_dict[node][k] * curr_val
          stack.append(k)
          if k == end: return visited[k]
    return -1.

if __name__ == '__main__':
  equations = [ ["a", "b"], ["b", "c"] ]
  values = [2.0, 3.0]
  queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
  a = Solution()
  print a.calcEquation(equations, values, queries)
