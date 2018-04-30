"""
667. Beautiful Arrangement II (Medium)

Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement: 
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.

Example 1:
Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
Example 2:
Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
Note:
The n and k are in the range 1 <= k < n <= 104.
"""

class Solution(object):
  def cons(self, n, k):
    if k == 1: return range(1, n+1)
    # solve first k
    min_ = 1
    max_ = k+1
    result = []
    while min_ <= max_:
      result.append(min_)
      min_ += 1
      if max_ > min_:
        result.append(max_)
        max_ -= 1
    tail = range(k+2, n+1)
    result = result + tail

    '''

    l2 = l2[::-1]
    print l1, l2
    result = []
    for i in range(len(l2)):
      result.append(l1[i])
      result.append(l2[i])
    if len(l1)>len(l2): result.append(l1[-1])
    print result
    tail = range(k+2, n+1)
    result = result + tail
    '''
    return result


if __name__ == "__main__":
  a = Solution()
  # print a.cons(3,1) 
  res = a.cons(100,40)
  tmp_set = set()
  for i in range(len(res)-1):
    tmp_set.add( abs(res[i]-res[i+1]))
  print tmp_set, len(tmp_set)
