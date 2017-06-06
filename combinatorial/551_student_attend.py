'''
551 Student Attendance Record I (Easy)

You are given a string representing an attendance record for a student. The record only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
'''

class Solution(object):
  def checkRecord(self, s):
    """
    :type s: str
    :rtype: bool
    """
    n = len(s)
    if n == 0: return True
    rec_A = 0
    rec_L = 0
    for i in range(n):
      if s[i] == 'A':
        rec_L = 0
        rec_A += 1
        if rec_A >= 2: return False
      elif s[i] == 'L':
        rec_L += 1
        if rec_L >= 3: return False
      else:  # Present
        rec_L = 0
    return True


if __name__ == '__main__':
  a = Solution()
  print a.checkRecord('PPALLP')
  print a.checkRecord('PPALLL')
