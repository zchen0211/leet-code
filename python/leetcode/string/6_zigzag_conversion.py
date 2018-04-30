'''
6. ZigZag Conversion (Medium)

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

class Solution(object):
  def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1: return s

    if numRows == 2:
      s1 = s[::2]
      s2 = s[1::2]
      return s1+s2

    n = len(s)
    matrix = []
    for i in range(numRows):
      matrix.append("")

    order = True
    id_ = 0
    for i in range(n):
      c = s[i]
      matrix[id_] = matrix[id_] + c
      if order:
        id_ += 1
        if id_ == numRows:
          id_ = numRows - 2
          order = False
      else:
        id_ -= 1
        if id_ == 0: order = True
    print matrix
    result = ""
    for item in matrix:
      result += item
    return result


if __name__ == "__main__":
  a = Solution()
  print a.convert("PAYPALISHIRING", 3)
  print a.convert("PAYPALISHIRING", 2)
