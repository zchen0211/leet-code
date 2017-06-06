'''
207. Course Schedule (Medium)

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
'''

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        remain = {}
        for i in range(numCourses):
            remain[i] = 0
        out_map = {}
        # update in-degree and out-going map
        for item in prerequisites:
            out_, in_ = item
            remain[out_] += 1
            # print out_, in_
            if out_map.has_key(in_):
                out_map[in_].append(out_)
            else:
                out_map[in_] = [out_]
        print out_map
                
        while(len(remain)!=0 and min(remain.values())==0):
            # remove all nodes with 0 in-degree, then itself from remain
            for k, v in remain.items():
                if v == 0:
                    # remove all edges
                    if out_map.has_key(k):
                        for i in out_map[k]:
                            # print 'i', i
                            remain[i] -= 1
                    # remove k
                    del(remain[k])
                    
                    break
        return len(remain) == 0
