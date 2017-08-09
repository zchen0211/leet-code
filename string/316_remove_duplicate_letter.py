'''
316. Remove Duplicate Letters (Hard)

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"
'''

class Solution(object):
  def removeDuplicateLetters(self, s):
    """
    :type s: str
    :rtype: str
    """
    stat = [[] for i in range(26)]
    for i in range(len(s)):
      n = ord(s[i]) - ord('a')
      stat[n].append(i)
    print 'initial: ', stat
    visited = set()
    result = ""
    min_ = 0
    cur_ptr = [0] * 26

    for i in range(26):
      # decide which char for result[i]
      # go through 'a' to 'z'
      # if not visited and not blocking other char not visited
      print i, 'th: '
      for j in range(26):
        c = chr(ord('a')+j)
        # print 'try ', c,
        if c in visited: continue
        if len(stat[j]) == 0: continue # not existing
        cur_pos = stat[j][0]
        # print cur_pos
        avail = True

        for jj in range(26):
          cc = chr(ord('a') + jj)
          if jj == j: continue
          if cc in visited: continue
          if len(stat[jj]) == 0: continue # not existing
          if cur_pos > stat[jj][-1]:
            avail = False
            break
        if avail: # can put char c
          print c, " available", cur_pos
          result += c
          visited.add(c)
          min_ = cur_pos
          for jj in range(26):
            while len(stat[jj])>0 and stat[jj][0]<=min_:
              stat[jj].remove(stat[jj][0])
          print 'visited', visited, 'stat', stat
          break
    return result


if __name__ == "__main__":
  a = Solution()
  print a.removeDuplicateLetters("bcabc")
  print a.removeDuplicateLetters("cbacdcbc")
