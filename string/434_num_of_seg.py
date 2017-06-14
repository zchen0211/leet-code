'''
434. Number of Segments in a String (Easy)

Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
'''

class Solution(object):
  def countSeg(self, s):
    cnt = 0
    if len(s) == 0:
      return cnt
    i = 0
    Flag = True
    while(i<len(s)):
      if s[i] != ' ' and Flag:
        cnt += 1
        Flag = False
      elif s[i] == ' ':
        Flag = True
      i += 1
    return cnt

  def solution2(self, s):
    s = ' '.join(s.split())
    print len(s)
    if len(s) == 0: return 0
    s_split = s.split(' ')
    print s_split
    return len(s_split)

if __name__ == '__main__':
  a = Solution()
  print a.countSeg("Hello, my name is John")
  print a.solution2("Hello,     my name is John")
  print a.solution2("    ")
  print a.solution2(", , , ,        a, eaefa")
