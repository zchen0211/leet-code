'''
7. Reverse Integer (Easy)

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 0
        neg_flag = x < 0
        x = abs(x)
        result = 0
        while x > 0:
            tmp = x % 10
            result = result * 10 + tmp
            x /= 10
        if neg_flag: result = -result
        
        if result > 2**31 - 1:
            return 0
        elif result < -2**31:
            return 0
        else:
            return result       
