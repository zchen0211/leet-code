"""
466. Count The Repetitions (Hard)

Define S = [s,n] as the string S which consists of n connected strings s. For example, ["abc", 3] ="abcabcabc".

On the other hand, we define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1. For example, 'abc' can be obtained from 'abdbec' based on our definition, but it can not be obtained from 'acbbe'.

You are given two non-empty strings s1 and s2 (each at most 100 characters long) and two integers 0 <= n1 <= 10**6 and 1 <= n2 <= 10**6. Now consider the strings S1 and S2, where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S2,M] can be obtained from S1.

Example:

Input:
s1="acb", n1=4
s2="ab", n2=2

Return:
2
"""

import re
class Solution(object):
    def solution2(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        formally the problem can be expressed as a regex problem of pattern='.*?'.join(list(s2)) and string=s1*n1
        """
        k=0
        i=0
        repeatTimes=0
        nextIdx=0
        posRest=['a']
        reps=['a']
        foundRep=False
        while not foundRep:
            i+=1
            for j in xrange(0,len(s1)):
                if s1[j]==s2[nextIdx]:
                    nextIdx+=1
                    if nextIdx==len(s2):
                        repeatTimes+=1
                        nextIdx=0
            posRest.append(nextIdx)
            reps.append(repeatTimes)
            if i>=n1:
                return repeatTimes/n2
            for k in xrange(0,i):
                if posRest[k]==nextIdx:
                    foundRep=True
                    break
            
        interval=i-k
        repeatCount=(n1-k)/interval
        print i,k,reps
        repeatTimes=repeatCount*(reps[i]-reps[k])
        remainTimes=reps[(n1-k)%interval+k]
        return (repeatTimes+remainTimes)/n2
  def getMaxRepetitions(self, s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    # stat of characters
    for c in s2:
      if c not in s1: return 0

    lut = self.helper(s1, s2)

    # cdg
    max_, min_ = max(n1, n2), min(n1, n2)
    cdg = self.cdg(max_, min_)
    print 'cdg', cdg
    n1, n2 = n1/cdg, n2/cdg
    print lut
    # check how many times s2 can be appeared in s1
    cnt = 0
    result = 0
    ns1 = len(s1)
    while cnt < ns1*n1:
      tmp = cnt % ns1
      cnt += lut[tmp]
      print 'old', s1[tmp], 'new', s1[cnt%ns1]
      if cnt <= ns1*n1: result += 1
    return result/n2

  def helper(self, s1, s2):
    # from 0 to len(s1)-1
    result = []
    ns1 = len(s1)
    ns2 = len(s2)
    for i in range(ns1):
      tmps1 = s1
      i1 = i
      i2 = 0
      cnt = 0
      while i2 != ns2:
        cnt += 1
        if s1[i1] == s2[i2]:
          i2 = i2 + 1
        i1 = (i1+1) % len(s1)
      result.append(cnt)
    return result

  def solve2(self, s1, n1, s2, n2):
    """
    :type s1: str
    :type n1: int
    :type s2: str
    :type n2: int
    :rtype: int
    """
    if n1 == 0: return 0
    # stat of characters
    for c in s2:
      if c not in s1: return 0

    lut = self.helper2(s1, s2)

    # cdg
    max_, min_ = max(n1, n2), min(n1, n2)
    cdg = self.cdg(max_, min_)
    print 'cdg', cdg
    n1, n2 = n1/cdg, n2/cdg

    print lut

    # check how many times s2 can be appeared in s1
    pos = 0
    cnt = 0
    for i in range(n1):
      tmp_pos, tmp_cnt = lut[pos]
      cnt += tmp_cnt
      pos = tmp_pos
    return cnt/n2

  def helper2(self, s1, s2):
    result = []
    # from 0 to len(s2)-1
    ns1 = len(s1)
    ns2 = len(s2)
    for i in range(ns2):
      tmps2 = s2
      i1 = 0
      i2 = i
      cnt = 0
      while i1 != ns1:
        if s1[i1] == s2[i2]:
          i2 += 1
        if i2 == ns2:
          cnt += 1
          i2 = 0
        i1 += 1
      result.append((i2, cnt))
    return result
 
  def cdg(self, max_, min_):
    if max_ % min_ == 0: return min_
    else:
      return self.cdg(min_, max_%min_)

if __name__ == '__main__':
  a = Solution()
  # print a.helper2('aba', 'ba')
  print a.getMaxRepetitions('acb', 4, 'ab', 2)
  print a.solve2('acb', 4, 'ab', 2)
  print a.getMaxRepetitions('aaa', 4, 'a', 1)
  print a.solve2('aaa', 4, 'a', 1)
  print a.getMaxRepetitions("nlhqgllunmelayl", 2, "lnl", 1)
  print a.solve2("nlhqgllunmelayl", 2, "lnl", 1)
  print a.getMaxRepetitions("caahumeayllfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikeffmznimkkasvwsrenazkycxaa", 1,"aac", 1)
  print a.solve2("caahumeayllfdxfircvscxggbwkfnqduxwfnfozvsrtkjprepggxrpnrvystmwcysyycqpevikeffmznimkkasvwsrenazkycxaa", 1,"aac", 1)
