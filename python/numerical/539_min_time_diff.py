'''
539. Minimum Time Difference (Medium)

Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.

Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
'''

class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        n = len(timePoints)
        timePoints.sort()
        tmp_diff = 24 * 60
        for i in range(0, n-1):
          t1 = timePoints[i]
          t2 = timePoints[i+1]
          h1, m1 = t1.split(':')
          h2, m2 = t2.split(':')
          h1, m1, h2, m2 = int(h1), int(m1), int(h2), int(m2)
          tmp_diff = min(tmp_diff, (h2-h1)*60+m2-m1)
        print tmp_diff
        # compute round clock diff
        t1 = timePoints[0]
        h1, m1 = t1.split(':')
        h1, m1 = int(h1), int(m1)
        tmp_d1 = h1*60 + m1
          
        t2 = timePoints[i+1]
        h2, m2 = t2.split(':')
        h2, m2 = int(h2), int(m2)
        tmp_d2 = (24-h2)*60 - m2
        return min(tmp_diff, tmp_d1+tmp_d2)


if __name__ == '__main__':
  a = Solution()
  print a.findMinDifference(['23:59','00:00'])
