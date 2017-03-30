'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.
'''

class Solution(object):
  def calculate(self, s):
    s_split = []
    n = len(s)
    i = 0
    # split it
    st = 0
    while(i<n):
      if s[i] == ' ':
        i += 1
      elif s[i] in ['+', '-', '*', '/']:
        s_split.append(s[i])
        i += 1
      else:
        st = i
        while(i!=n-1 and s[i+1] not in [' ', '+', '-', '*', '/']):
          i += 1
        s_split.append(int(s[st:i+1]))
        i += 1
    # eval
    if s_split[0] == '-':
      del s_split[0]
      s_split[0] = -s_split[0]

    base = 0
    neg_flag = False
    curr = s_split[0]
    if curr<0:
      curr = -curr
      neg_flag = True
    i = 1
    while(i<len(s_split)):
      if s_split[i] == '*':
        curr = curr * s_split[i+1]
      elif s_split[i] == '/':
        curr = curr // s_split[i+1]
      else:
        if neg_flag:
          base -= curr
        else:
          base += curr
        curr = s_split[i+1]
        neg_flag = False
        if s_split[i] == '-':
          neg_flag = True
      i += 2
      print base, curr
    if not neg_flag:
      base += curr
    else:
      base -= curr
    return base

if __name__ == '__main__':
  a = Solution()
  '''print a.calculate("3+2*2")
  print a.calculate(" 3/2 ")
  print a.calculate(" 3+5 / 2 ")
  print a.calculate(' 1  ')
  print a.calculate(' -2 ')
  print a.calculate('-2 - 3 * 4')'''
  print a.calculate('14 - 3 /2')  
