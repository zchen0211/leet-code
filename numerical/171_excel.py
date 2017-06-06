'''
171. Excel Sheet Column Number (Easy)

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp_dic ={}
        for i in range(1,27):
            tmp_dic[str(unichr(ord('A')+i-1))] = i
        cnt = 0
        s = s[::-1]
        i = 0
        for i in range(len(s)):
            c = s[i]
            cnt += tmp_dic[c] * (26**i)
        return cnt
