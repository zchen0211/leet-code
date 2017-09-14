'''
537. Complex Number Multiplication (Medium)

Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.

Note:
The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.
'''

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_r, a_i = a.split('+')
        b_r, b_i = b.split('+')
        a_r, b_r = int(a_r), int(b_r)
        a_i, b_i = int(a_i[:-1]), int(b_i[:-1])
        
        c_r = a_r*b_r - a_i*b_i
        c_i = a_i*b_r + a_r*b_i
        result = str(c_r)+'+'+str(c_i)+'i'
        return result


if __name__ == '__main__':
  a = Solution()
  print a.complexNumberMultiply('1+1i', '1+1i')
  print a.complexNumberMultiply('1+-1i', '1+-1i')
