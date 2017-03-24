class Solution(object):
  def findAnagrams(self, s, p):
    # construct a set list
    p_set = {}
    for p_char in p:
      if p_set.has_key(p_char):
        p_set[p_char] += 1
      else:
        p_set[p_char] = 1
    # go through s
    p_len = len(p)
    s_len = len(s)
    s_set = {}
    s_set_cnt = 0
    result = []
    for i in range(s_len):
      # add s[i], s_set_cnt++
      if s_set.has_key(s[i]):
        s_set[s[i]] += 1
      else:
        s_set[s[i]] = 1
      s_set_cnt += 1
      # if s_set_cnt == p_len + 1, remove s[i-p_len()] from s_set
      if s_set_cnt == p_len + 1:
        tmp_c = s[i-p_len]
        s_set[tmp_c] -= 1
        s_set_cnt -= 1
        if s_set[tmp_c] == 0:
          s_set.pop(tmp_c)
      # if set equal, add i-p_len
      if s_set_cnt == p_len and s_set == p_set:
        result.append(i-p_len+1)
    return result


if __name__ == '__main__':
  a = Solution()
  print a.findAnagrams("cbaebabacd", 'abc')
