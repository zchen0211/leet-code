'''
168. Excel Sheet Column Title (Easy)

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
'''

# 1-26: A-Z
# 26 + 1..26*26: AA..ZZ
# cumul + 1..26*26*26:
class Solution(object):
  def convertToTitle(self, n):
    """
    :type n: int
    :rtype: str
    """
    cumul = 0
    tmp_dic = {}
    for i in range(1, 27):
      tmp_dic[i] = str(unichr(ord('A')+i-1))
    i = 1
    while(True):
      cumul_after = cumul + 26 ** i
      if n>cumul and n<=cumul_after:
        result = ''
        while(n>0):
          rem = (n-1)%26 +1
          n = (n-rem)/26
          tmp_c = tmp_dic[rem]
          result += tmp_c
          # print rem, tmp_c
        if len(result) < i:
          result += 'A'*(i-len(result))
        result = result[::-1]
        return result
      else:
        cumul = cumul_after
        i += 1


if __name__ == '__main__':
  a = Solution()
  print a.convertToTitle(26)
  print a.convertToTitle(28)
  print a.convertToTitle(26+26*26+26**3)
  
