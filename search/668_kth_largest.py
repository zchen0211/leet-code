"""
668. Kth largest Number in Multiplication Table (Hard)

Nearly every one have used the Multiplication Table. But could you find out the k-th largest number quickly from the multiplication table?

Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return the k-th largest number in this table.

Example 1:
Input: m = 3, n = 3, k = 5
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6
3	6	9

The 5-th largest number is 3 (1, 2, 2, 3, 3).
Example 2:
Input: m = 2, n = 3, k = 6
Output: 
Explanation: 
The Multiplication Table:
1	2	3
2	4	6

The 6-th largest number is 6 (1, 2, 2, 3, 4, 6).
Note:
The m and n will be in the range [1, 30000].
The k will be in the range [1, m * n]
"""

class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        min_ = 1
        max_ = m*n

        while min_ < max_:
          mid = (min_+max_) / 2
          valid_, cnt = helper(m, n, mid)
          # print valid_, cnt
          if k == cnt:
            return valid_
          elif k > cnt:
            min_ = mid+1
          else:
            max_ = mid
        return min_


def helper(m, n, val):
  # return max_, cnt
  max_ = 1
  cnt = 0
  for i in range(1, m+1):
    # tmp_m == i
    tmp = min(n, val/i)
    cnt += tmp
    max_ = max(max_, tmp*i)
  return max_, cnt


if __name__ == "__main__":
  a = Solution()
  print a.findKthNumber(100,100,4000)
