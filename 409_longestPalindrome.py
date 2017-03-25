class Solution(object):
  def longestPalindrome(self, s):
    if not s:
      return 0
    count_dict = {}
    for i in range(len(s)):
      if count_dict.has_key(s[i]):
        count_dict[s[i]] += 1
      else:
        count_dict[s[i]] = 1
    odd_flag = False
    cnt = 0
    for _, v in count_dict.items():
      if v % 2 == 1:
        odd_flag = True
        cnt += v-1
      else:
        cnt += v
    if odd_flag:
      cnt += 1
    return cnt


if __name__ == '__main__':
  a = Solution()
  print a.longestPalindrome('abccccdd')
