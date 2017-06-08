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

    stack = []
    n = len(s)
    i = 0
    while(i<n):
      if s[i] in ['(', ')', '+', '-', '*', '/']:
        stack.append(s[i])
        i += 1
      else:
        start = i
        end = start
        while(end<n and s[end] not in ['+','-','*','/','(',')']):
          end += 1
        stack.append(int(s[start:end]))
        i = end
    print stack

    # eval
    new_stack = []
    n = len(stack)
    for i in range(n):
      if stack[i] == '(': new_stack.append(item)
      elif stack[i] == ')':
        # eval the thing in '('
        
  def helper(self, stack):
    new_stack = []
    n = len(stack)
    i = 0
    # remove all '(', ')'
    while(i<n):
      if stack[i] == '(':
        start, end = i, i+1
        cnt = 1
        while(cnt>0):
          if stack[end] == '(': cnt += 1
          elif stack[end] == ')': cnt -= 1
          end += 1
        result = self.helper(stack[start+1:end])
        new_stack.append(result)
        i = end
      else:
        new_stack.append(stack[i])
        i += 1
    # eval
    base = 0
    i = 0
    final_stack = []
    if new_stack[0] == '-':
      final_stack.append(-new_stack[1])
      i = 2
    else:
      final_stack.append(new_stack[0])
      i = 1
    while(i<len(new_stack)):
      if new_stack[i] == '+':
        final_stack.append(new_stack[i+1])
      elif new_stack[i] == '-':
        final_stack.append(-new_stack[i+1])
      elif new_stack[i] == '*':
        final_stack[-1] = final_stack[-1] * new_stack[i+1]
      elif new_stack[i] == '/':
        final_stack[-1] = final_stack[-1] / new_stack[i+1]
    return sum(final_stack)

if __name__ == '__main__':
  a = Solution()
  print a.calculate("1 + 1")
  print a.calculate(" 2-1 + 2 ")
  print a.calculate("(1+(4+5+2)-3)+(6+8)")
