class Solution(object):
  def licenseKeyFormatting(self, S, K):
    # go through S
    cnt = 0
    output = ''
    for i in range(len(S)):
      if S[i] != '-':
        cnt += 1
    if cnt == 0:
      return ''
    # generate output
    tmp_cnt = K - cnt % K # to save mod
    tmp_pos = 0
    while(tmp_pos<len(S)):
      if S[tmp_pos] == '-':
        tmp_pos += 1
      else:
        output += S[tmp_pos]
        tmp_cnt += 1
        if tmp_cnt % K == 0:
          tmp_cnt = 0
          output += '-'
        tmp_pos += 1
    if output[-1] == '-':
      output = output[:-1]
    return output.upper()


if __name__ == '__main__':
  a = Solution()
  print a.licenseKeyFormatting("2-4A0r7-4k", K = 5)
  print a.licenseKeyFormatting("---", K = 3)
