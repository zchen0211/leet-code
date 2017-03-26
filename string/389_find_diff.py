class Solution(object):
  def findTheDifference(self, s, t):
    count_s = {}
    count_t = {}
    for i in range(len(s)):
      if count_s.has_key(s[i]):
        count_s[s[i]] += 1
      else:
        count_s[s[i]] = 1

    for i in range(len(t)):
      if count_t.has_key(t[i]):
        count_t[t[i]] += 1
      else:
        count_t[t[i]] = 1
   
    for k, v in count_t.items():
      if not count_s.has_key(k) or v == count_s[k]+1:
        return k


if __name__ == '__main__':
  a = Solution()
  print a.findTheDifference('abcd','abcde')
