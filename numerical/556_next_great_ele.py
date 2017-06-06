'''
556. Next Greater Element III (Medium)

Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:
Input: 12
Output: 21
Example 2:
Input: 21
Output: -1
'''

class Solution(object):
  def nextGreaterElement(self, n):
    """
    :type n: int
    :rtype: int
    """
    if n < 10: return -1

    # first break into single digit
    digit = []
    while(n>0):
      digit.append(n % 10)
      n = n / 10
    n_digit = len(digit)
    digit = digit[::-1]

    # find first reverse order digit
    i = n_digit-1
    while(i>0 and digit[i]<=digit[i-1]):
      i -= 1
    if i == 0: # doesn't exist
      return -1

    # i-th digit reverse
    # find smallest number in tmp[i:] > tmp[i]
    larger = digit[i]
    larger_id = i
    for j in range(i+1, n_digit):
      if digit[j] > digit[i-1]:
        larger = min(larger, digit[j])
        larger_id = j
    print i
    # swap (i-1)-th and larger_id'th digit
    digit[i-1], digit[larger_id] = digit[larger_id], digit[i-1]
    tail = digit[i:]
    tail.sort()
    # if tail is None: tail = []
    digit = digit[:i] + tail
    result = 0
    for item in digit:
      result = result * 10 + item
    if result > 2147483647: return -1
    return result


if __name__ == '__main__':
  a = Solution()
  print a.nextGreaterElement(21)
  print a.nextGreaterElement(39721)
