'''
639. Decode Ways II My SubmissionsBack to Contest (Hard)

A message containing letters from A-Z is being encoded to numbers using the following mapping way:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.

Given the encoded message containing digits and the character '*', return the total number of ways to decode it.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
Example 2:
Input: "1*"
Output: 9 + 9 = 18
Note:
The length of the input string will fit in range [1, 105].
The input string will only contain the character '*' and digits '0' - '9'.
'''

import time

class Solution(object):
    def helper1(self, s, i): # decode 1 digit
        if s[i] == '0':
           return 0
        elif s[i] != '*':
            return 1
        else:
            return 9
    
    def helper2(self, s, i):
        if s[i] == '*' and s[i+1] == '*': # case 1: **
            return 15
        elif s[i] != '*' and s[i+1] == '*': # case 2: d*
            if s[i] == '1': return 9
            elif s[i] == '2': return 6
            else: return 0
        elif s[i] == '*' and s[i+1] != '*': # case 3: *d
            if s[i+1] in set(['7','8','9']): # split + 17/18/19
                return 1
            else: 
                return 2
        else: # case 4: 'dd'
            n = int(s[i:i+2])
            if s[i] != '0' and n >=1 and n <= 26 :
                return 1
            else:
                return 0
        
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        
        # initial condition
        a = self.helper1(s,0)
        if len(s) == 1: return a
        
        b = self.helper1(s, 0)*self.helper1(s,1) + self.helper2(s, 0)
        if len(s) == 2: return b
        
        i = 2
        MOD = 10**9 + 7
        print a, b
        while i < len(s):
            new = 0
            # a + s[i-1,i]
            new += a * self.helper2(s, i-1)
            
            # b + s[i]
            new += b * self.helper1(s,i)
            a, b = b % MOD, new % MOD
            i += 1
        return b

if __name__ == '__main__':
    a = Solution()
    print a.numDecodings('1*')
    t = time.time()
    fi = open('input', 'r')
    s = fi.readlines()
    s = s[0][1:-2]
    # print a.numDecodings("*10*1")
    print a.numDecodings(s)
    print time.time() - t
