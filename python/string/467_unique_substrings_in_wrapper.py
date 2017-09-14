"""
467. Unique Substrings in Wraparound String (Medium)

Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string strings.
Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.
"""

class Solution(object):
  def findSubstringInWraproundString(self, p):
    """
    :type p: str
    :rtype: int
    """
    n = len(p)
    if n == 0: return 0
    stat = {}
    i = 0
    start = 0
    while i<n:
      if i==n-1 or not self.is_next(p[i+1], p[i]):
        # conclude p[start] to p[i]
        while start != i+1:
          tmp = p[start]
          if tmp not in stat: stat[tmp] = i-start+1
          else: stat[tmp] = max(stat[tmp], i-start+1)
          start += 1 
      i += 1
    print stat
    return sum(stat.values())

  def is_next(self, si, sj):
    if ord(si) - ord(sj) == 1:
      return True
    elif si == 'a' and sj == 'z':
      return True
    return False


if __name__ == '__main__':
  a = Solution()
  print a.findSubstringInWraproundString('zab')
  print a.findSubstringInWraproundString('cac')
  print a.findSubstringInWraproundString('a')
