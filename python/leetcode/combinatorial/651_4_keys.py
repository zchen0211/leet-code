"""
651. 4 Keys Keyboard (Medium)

Imagine you have a special keyboard with the following keys:

Key 1: (A): Prints one 'A' on screen.

Key 2: (Ctrl-A): Select the whole screen.

Key 3: (Ctrl-C): Copy selection to buffer.

Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.

Example 1:
Input: N = 3
Output: 3
Explanation: 
We can at most get 3 A's on screen by pressing following key sequence:
A, A, A
Example 2:
Input: N = 7
Output: 9
Explanation: 
We can at most get 9 A's on screen by pressing following key sequence:
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
Note:
1 <= N <= 50
Answers will be in the range of 32-bit signed integer.

"""

class Solution(object):
  def maxA(self, N):
    """
    :type N: int
    :rtype: int
    """
    max_ = range(0, N+1)

    for i in range(4, N+1):
      # compute max_[i]
      j = i-3
      while j>=3:
        max_[i] = max(max_[i], max_[j]*(i-j-1))
        j -= 1
      print i, max_[i]
    return max_[-1]


if __name__ == "__main__":
  a = Solution()
  print a.maxA(10)
