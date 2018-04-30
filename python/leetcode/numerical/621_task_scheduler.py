"""
621. Task Scheduler My SubmissionsBack To Contest (Medium)

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ['A','A','A','B','B','B'], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
"""
import collections

class Solution(object):
  def leastInterval(self, tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    stat = dict(collections.Counter(tasks))
    val = stat.values()
    val.sort()
    v_max = max(val) # times of the most frequent item
    max_cnt = val.count(v_max)
    result1 = len(tasks)
    result2 = (v_max-1) * (n+1) + max_cnt
    return max(result1, result2)


if __name__ == '__main__':
  a = Solution()
  print a.leastInterval(['A','A','A','B','B','B'], 2)
