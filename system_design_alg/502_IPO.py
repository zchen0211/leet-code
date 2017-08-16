"""
502. IPO (Hard)

Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given several projects. For each project i, it has a pure profit Pi and a minimum capital of Ci is needed to start the corresponding project. Initially, you have W capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

To sum up, pick a list of at most k distinct projects from given projects to maximize your final capital, and output your final maximized capital.

Example 1:
Input: k=2, W=0, Profits=[1,2,3], Capital=[0,1,1].

Output: 4

Explanation: Since your initial capital is 0, you can only start the project indexed 0.
             After finishing it you will obtain profit 1 and your capital becomes 1.
             With capital 1, you can either start the project indexed 1 or the project indexed 2.
             Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
             Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
Note:
You may assume all numbers in the input are non-negative integers.
The length of Profits array and Capital array will not exceed 50,000.
The answer is guaranteed to fit in a 32-bit signed integer.
"""
import Queue

class Solution(object):
  def findMaximizedCapital(self, k, W, Profits, Capital):
    """
    :type k: int
    :type W: int
    :type Profits: List[int]
    :type Capital: List[int]
    :rtype: int
    """
    # Correct logic, but will TLE
    n = len(Profits)
    arrange = [(Profits[i],Capital[i]) for i in range(n)]
    arrange.sort(reverse=True)
    print arrange
    for i in range(k):
      for j in range(len(arrange)):
        p, c = arrange[j]
        print p,c
        if c<= W:
          print 'pick', p, c
          W += p
          break
      if j < len(arrange):
        del arrange[j]
    return W

  def solution2(self, k, W, Profits, Capital):
    q_cap = Queue.PriorityQueue() # capital min-heap
    q_pro = Queue.PriorityQueue() # profits max-heap
    n = len(Profits)
    for i in range(n):
      c, p = Capital[i], Profits[i]
      q_cap.put((c,p))

    while k>0:
      # pick one add into W
      while q_cap.qsize() > 0:
        c, p = q_cap.get()
        if c <= W: q_pro.put((-p,c))
        else:
          q_cap.put((c,p)) # put back
          break
      if q_pro.qsize() > 0:
        p, c = q_pro.get()
        W -= p
      else: break
      k -= 1
    return W

if __name__ == '__main__':
  a = Solution()
  # print a.findMaximizedCapital(1, 2, [1,2,3], [1,1,2])
  print a.solution2(1, 0, [1,2,3], [1,1,2])
