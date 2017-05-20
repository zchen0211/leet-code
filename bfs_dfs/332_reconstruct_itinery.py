'''
332. Reconstruct Itinerary (Euler Path)
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
'''
import collections

class Solution(object):
  def findItinery(self, tickets):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    # dict construction first
    map_dep_arr = {}
    for item in tickets:
      dep, arr = item
      if dep in map_dep_arr:
        map_dep_arr[dep].append(arr)
      else:
        map_dep_arr[dep] = [arr]
    # sort
    for k in map_dep_arr:
      map_dep_arr[k].sort()
      map_dep_arr[k].sort()

    # dfs
    result = ['JFK']
    curr = 'JFK'
    cnt = 0
    while(cnt < len(tickets)):
      # arrive at a new place
      arr = map_dep_arr[curr][0]
      result.append(arr)
      del map_dep_arr[curr][0]
      curr = arr
      # inc
      cnt += 1
      print result
    return result

  def findItinery2(self, tickets):
    targets = collections.defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
      targets[a] += b,
    print targets
    route = []
    def visit(airport):
      while targets[airport]:
        visit(targets[airport].pop())
      route.append(airport)
      print route
    visit('JFK')
    return route[::-1]

if __name__ == '__main__':
  a = Solution()
  # print a.findItinery2([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
  # print a.findItinery2([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
  # print a.findItinery2([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])
  print a.findItinery2([["JFK","1"],["1","JFK"],["2","JFK"],['JFK','2']])
