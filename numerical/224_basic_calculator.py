'''
224. Basic Calculator (Hard)

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23
Note: Do not use the eval built-in library function.
'''

class Solution(object):
  def calculate(self, s):
    """
    :type s: str
    :rtype: int
    """
    # remove spaces
    s = s.replace(' ', '')
    stack = [1]
    n = len(s)

    i = 0
    result = 0
    curr_num = 0
    while i < n:
      sgn = +1 # sign
      # digit, consume all digit
      if ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
        # print 'here'
        if i > 0 and s[i-1] == '-': sgn = -1
        while i < n and ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'):
          curr_num = curr_num * 10 + ord(s[i]) - ord('0')
          i += 1
        result += sgn * stack[-1] * curr_num
        # print curr_num, result
        curr_num = 0
        continue 
      else:
        # (
        if s[i] == '(':
          if i >= 1 and s[i-1] == '-': stack.append(-stack[-1])
          else: stack.append(stack[-1])
        # )
        elif s[i] == ')':
          stack.pop()
          if not stack: stack.append(1)
        # print stack
      i += 1
    return result


if __name__ == '__main__':
  a = Solution()
  print a.calculate("1 + 1")
  print a.calculate(" 2-1 + 2 ")
  print a.calculate("(1+(4+5+2)-3)+(6+8)")
  print a.calculate("(7)-(0)+(4)")
