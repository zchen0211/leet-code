'''
here are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
'''

class Solution(object):
  def findOrder(self, numCourses, prerequisites):
    edge_dict = {}
    degree_list = [0] * numCourses
    _zero_degree_list = []
    for post_, pre_ in prerequisites:
      if pre_ in edge_dict:
        edge_dict[pre_].append(post_)
      else:
        edge_dict[pre_] = [post_]
      degree_list[post_] += 1
    # initialize _zero
    for i in range(len(degree_list)):
      if degree_list[i] == 0:
        _zero_degree_list.append(i)

    result = []
    while(len(_zero_degree_list) !=0): # not empty
      # remove edge and update degree_list
      i = _zero_degree_list.pop()
      if i in edge_dict:
        for j in edge_dict[i]:
          degree_list[j] -= 1
          # add to _zero if needed
          if degree_list[j] == 0:
            _zero_degree_list.append(j)
        # append to result
      result.append(i)

    if len(result) == numCourses:
      return result
    else:
      return []


if __name__ == '__main__':
  a = Solution()
  print a.findOrder(2, [[1,0]])
  print a.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])


