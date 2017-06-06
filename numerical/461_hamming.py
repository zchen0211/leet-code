'''
461. Hamming Distance (Easy)

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
'''

class Solution(object):
  def hammingDis(self, x, y):
    if x == 0 and y == 0:
      return 0
    cnt = 0
    while x > 0 or y > 0:
      x_rem = x % 2
      y_rem = y % 2
      x = x // 2
      y = y // 2
      if x_rem != y_rem:
        cnt += 1
    return cnt


if __name__ == '__main__':
  a = Solution()
  print a.hammingDis(3, 7)
