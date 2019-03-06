'''
552. Student Attendance Record II (Hard)

Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Example 1:
Input: n = 2
Output: 8 
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times. 
Note: The value of n won't exceed 100,000.
'''

class Solution(object):
  def checkRecord(self, n):
    """
    :type n: int
    :rtype: int
    """
    wA = [1, 0, 0, 0] # end with A, P, L, LL
    woA = [1, 1, 0] # end with P, L, LL
    for i in range(1, n):
      wA[0], wA[1], wA[2], wA[3] = sum(woA), sum(wA), sum(wA[0:2]), wA[2]
      woA[0], woA[1], woA[2] = sum(woA), woA[0], woA[1]
      for i in range(4):
        wA[i] = wA[i] % (10**9+7)
      for i in range(3):
        woA[i] = woA[i] % (10**9+7)
    result = (sum(wA) + sum(woA)) % (10**9+7)
    return result


if __name__ == '__main__':
  a = Solution()
  print a.checkRecord(1)
  print a.checkRecord(2)
  print a.checkRecord(3)
