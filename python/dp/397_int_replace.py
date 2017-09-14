"""
397. Integer Replacement (Medium)

Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
"""

class Solution(object):
  def integerReplacement(self, n):
    """
    :type n: int
    :rtype: int
    """
    # AC, memoized DP
    look_up_map = {1:0, 2:1, 3:2, 4:2}
    r = self.helper(n, look_up_map)
    print look_up_map
    return r
    
  def helper(self, n, look_up_map):
    offset = 0
    ori_n = n
    while(n%2==0):
      n /= 2
      offset += 1

    if n in look_up_map:
      look_up_map[ori_n] = look_up_map[n] + offset
      return offset + look_up_map[n]
    r1 = self.helper(n+1, look_up_map)
    r2 = self.helper(n-1, look_up_map)
    result = min(r1, r2) + 1 + offset
    look_up_map[ori_n] = result
    return result

  def solve(self, n):
    # AC: much faster
    # pay attention to the special case n==3
    if n == 1: return 0
    cnt = 0
    while n>1:
      if n % 2 == 0: n /= 2
      elif n % 4 == 3 and n!=3: n += 1
      else: n -= 1
      cnt += 1
    return cnt

if __name__ == '__main__':
  a = Solution()
  # print a.integerReplacement(16)
  # print a.integerReplacement(7)
  print a.integerReplacement(1234)
