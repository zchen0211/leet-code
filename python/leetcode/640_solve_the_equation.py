'''
640. Solve the Equation (Medium)

Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"
'''

class Solution(object):
  def solve(self, equation):
    l1, l2 = equation.split('=')
    print l1, l2
    x_co1, co1 = self.parse(l1)
    x_co2, co2 = self.parse(l2)
    if x_co1 == x_co2:
      if co1 == co2:
        return "Infinite solutions"
      else:
        return "No solution"
    x_co = x_co1 - x_co2
    co = co2 - co1
    final = co / x_co
    return 'x='+str(final)

  def parse(self, eq):
    if eq[0] != '-':
      eq = '+' + eq
    # parse
    x_co = 0
    co = 0
    i = 0
    n = len(eq)
    digit_set = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    while i < n:
      # first +/-
      pos_flag = (eq[i] == '+')
      i += 1
      j = i
      while j<n and eq[j] in digit_set:
        j += 1
      if i == j: num = 1
      else: num = int(eq[i:j])
      if not pos_flag: num = -num
      # print num
      # print 'j', j, eq[j]
      if j!=n and eq[j] == 'x':
        x_co += num
        j += 1
      else:
        co += num
      i = j
    print 'final', x_co, co
    return x_co, co

if __name__ == '__main__':
  a = Solution()
  print a.solve("x+5-3+x=6+x-2")
  print a.solve("x=x")
  print a.solve("2x=x")
  print a.solve("2x+3x-6x=x+2")
  print a.solve("x=x+2")
