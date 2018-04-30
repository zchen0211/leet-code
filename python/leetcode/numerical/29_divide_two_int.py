'''
29. Divide Two Integers (Medium)

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend * divisor > 0:
            neg = False
        else:
            neg = True
        dividend, divisor = abs(dividend), abs(divisor)
            
        result = 0
        while dividend >= divisor:
            cnt, div_ = 1, divisor
            while div_ < dividend / 2:
                cnt *= 2
                div_ *= 2
            dividend -= div_
            result += cnt
        if neg:
            return max(-result, -2**31)
        else:
            return min(result, 2**31-1)

if __name__ == "__main__":
    a = Solution()
    print a.divide(10, 2)
