"""
718. Maximum Length of Repeated Subarray (Medium)

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
Note:
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""

class Solution(object):
  def findLength(self, A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: int
    """
    nA, nB = len(A), len(B)
    ret = []
    for i in range(nA+1):
      ret.append([0] * (nB+1))

    for i in range(nA-1, -1, -1):
      for j in range(nB-1, -1, -1):
        if A[i] == B[j]:
          ret[i][j] = 1 + ret[i+1][j+1]
    result = max(ret[0])
    for i in range(1, nA):
      result = max(result, max(ret[i]))
    return result

if __name__ == "__main__":
  a = Solution()
  print a.findLength([1,2,3,2,1], [3,2,1,4,7])
  print a.findLength([0,1,1,1,1], [1,0,1,0,1])
 
