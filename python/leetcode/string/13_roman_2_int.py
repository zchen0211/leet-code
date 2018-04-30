'''
13. Roman to Integer (Easy)

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rec = []
        rec.append(('M', '-', '-'))
        rec.append(('C', 'D', 'M'))
        rec.append(('X', 'L', 'C'))
        rec.append(('I', 'V', 'X'))
        result = 0
        i = 0
        while s != '':
            tmp = 0
            c1, c2, c3 = rec[i]
            if s.startswith(c1+c2):
                tmp = 4
                s = s[2:]
            elif s.startswith(c1+c3):
                tmp = 9
                s = s[2:]
            else:
                if s.startswith(c2):
                    tmp = 5
                    s = s[1:]
                j = 0
                while j < len(s) and s[j] == c1:
                    j += 1
                tmp += j
                s = s[j:]
            result += tmp * (10 ** (3-i))          
            
            i += 1
        return result
