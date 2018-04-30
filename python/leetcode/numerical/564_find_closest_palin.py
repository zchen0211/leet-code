'''
564. Find the Closest Palindrome (Hard)

Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input: "123"
Output: "121"
Note:
The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
'''

class Solution(object):
  def nearestPalindromic(self, n):
    """
    :type n: str
    :rtype: str
    """
    if n == '0': return '1'
    # if len(n) == 1:
    #   return str(int(n)-1)

    n_list = []
    for i in range(len(n)): n_list.append(n[i])
    n_list = [int(item) for item in n_list]
    n_list_l = [item for item in n_list]
    n_list_l = self.helper_smaller(n_list_l)
    print 'small', n_list_l
    n_list_r = [item for item in n_list]
    n_list_r = self.helper_larger(n_list_r)
    print 'large', n_list_r
    diff1 = self.diff(n_list, n_list_l)
    print 'diff small', diff1
    diff2 = self.diff(n_list_r, n_list)
    print 'diff large', diff2
    if self.comp(diff2, diff1) >= 0:
      # n_list_l
      return ''.join([str(item) for item in n_list_l])
    else:
      # n_list_r
      return ''.join([str(item) for item in n_list_r])

  def comp(self, list1, list2):
    if len(list1) > len(list2): return 1
    elif len(list1) < len(list2): return -1
    i = 0
    while i < len(list1):
      if list1[i] > list2[i]: return 1
      elif list1[i] < list2[i]: return -1
      i += 1
    return 0

  def diff(self, list1, list2):
    tmpl1 = list1[::-1]
    tmpl2 = list2[::-1]
    carry = False
    i = 0
    ret = []
    while i < len(tmpl1):
      tmp1 = tmpl1[i]
      if i < len(tmpl2): tmp2 = tmpl2[i]
      else: tmp2 = 0
      if carry: tmp1 -= 1
      if tmp1 >= tmp2:
        ret.append(tmp1-tmp2)
        carry = False
      else:
        tmp1 += 10
        ret.append(tmp1-tmp2)
        carry = True
      i += 1
    ret = ret[::-1]
    while ret[0] == 0: del ret[0]
    return ret

  def isPalin(self, s):
    i = 0
    j = len(s)-1
    while i<j:
      if s[i] == s[j]:
        i, j = i+1, j-1
      else: return False
    return True

  def helper_smaller(self, s):
    n = len(s)
    if n % 2 == 1:
      i, j = (n-1)/2, (n-1)/2
    else:
      i, j = n/2-1, n/2

    if not self.isPalin(s):
      # print 'going here'
      left = s[0:i+1]
      left = left[::-1]
      left = ''.join([str(item) for item in left])
      right = s[j:]
      right = ''.join([str(item) for item in right])
      # print 'left', left
      # print 'right', right
      flag = right > left

      while i>=0:
        s[j] = s[i]
        i, j = i-1, j+1
      if flag: return s
    print 'now', s
    # decrese the first non-zero near center symmetrically
    if n % 2 == 1:
      i, j = (n-1)/2, (n-1)/2
    else:
      i, j = n/2-1, n/2
    while i>=0:
      if s[i] > 0:
        print 'here'
        s[i], s[j] = s[i]-1, s[j]-1 
        break
      i, j = i-1, j+1
    # if not 100001
    if sum(s) != 0 or len(s)==1: return s
    else: return [9]*(n-1)

  def helper_larger(self, s):
    n = len(s)
    if n % 2 == 1:
      i, j = (n-1)/2, (n-1)/2
    else:
      i, j = n/2-1, n/2

    if not self.isPalin(s):
      left = s[0:i+1]
      left = left[::-1]
      left = ''.join([str(item) for item in left])
      right = s[j:]
      right = ''.join([str(item) for item in right])
      flag = left > right

      while i>=0:
        s[j] = s[i]
        i, j = i-1, j+1
      if flag: return s
    # increse the first non-nine near center symmetrically
    if n % 2 == 1:
      i, j = (n-1)/2, (n-1)/2
    else:
      i, j = n/2-1, n/2
    while i>=0:
      if s[i] < 9:
        s[i], s[j] = s[i]+1, s[j]+1 
        break
      i, j = i-1, j+1
    # if not 9999
    if sum(s) != 9*n: return s
    else: return [1]+[0]*(n-1)+[1]


if __name__ == '__main__':
  a = Solution()
  for i in range(10):
    print i, a.nearestPalindromic(str(i))
  # print a.helper_smaller([1,2])
  # print a.helper_larger([1,2,4,3])
  # print a.diff([1,2,3], [1,0,9])
