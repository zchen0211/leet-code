"""
634. Find the Derangement of An Array My SubmissionsBack to Contest (Medium)

In combinatorial mathematics, a derangement is a permutation of the elements of a set, such that no element appears in its original position.

There's originally an array consisting of n integers from 1 to n in ascending order, you need to find the number of derangement it can generate.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: 3
Output: 2
Explanation: The original array is [1,2,3]. The two derangements are [2,3,1] and [3,1,2].
Note:
n is in the range of [1, 106].
"""

class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 0
        T = 1
        O = 0
        for i in range(2, n+1):
            T, O = i * O, (i-1)*O + T
            print i, T, O
        return O


if __name__ == '__main__':
  a = Solution()
  print a.findDerangement(13)
