'''
202. Happy Number (Easy)

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
'''

class Solution(object):
    def decode(self, n):
        result =[]
        while(n>0):
            result.append(n%10)
            n = n/10
        return result
        
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        tmp_set = set([n])
        while(n>1):
            tmp_set.add(n)
            result = self.decode(n)
            result = [item**2 for item in result]
            n = sum(result)
            if n in tmp_set and n != 1:
                return False
        return n==1
