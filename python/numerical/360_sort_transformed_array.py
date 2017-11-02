"""
360. Sort Transformed Array (Medium)

Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example:
nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

Result: [3, 9, 15, 33]

nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

Result: [-23, -5, 1, 7]
"""

class Solution(object):
  def sortTransformedArray(self, nums, a, b, c):
    """
    :type nums: List[int]
    :type a: int
    :type b: int
    :type c: int
    :rtype: List[int]
    """
    n = len(nums)
    if n == 0: return []
    if a != 0:
      axis = -float(b) / float(2*a)
      nums_ = self.arrange_sym(nums, axis)
    else:
      nums_ = nums

    ret = [a*item*item+b*item+c for item in nums_]
    if ret[0] > ret[-1]:
      ret = ret[::-1]
    return ret

  def arrange_sym(self, nums, axis):
    if axis < nums[0]:
      return nums
    if axis > nums[-1]:
      return nums
    # look for the nearest num to axis
    n = len(nums)
    i, j = 0, n - 1
    while i < j:
      mid = (i + j) / 2
      if abs(nums[mid] - axis) < 0.5:
        i, j = mid, mid
        break
      elif nums[mid] > axis:
        j = mid - 1
      else:
        i = mid + 1
    i = min(i, j)
    if nums[i] > axis:
      i, j = i-1, i
    else:
      i, j = i, i+1
    nums_ = []
    print 'axis', axis
    while i >= 0 or j < n:
      print i,j,
      # if j == n or abs(nums[i]-axis) <= abs(nums[j]-axis):
      if i >=0 and (j == n or abs(nums[i]-axis) <= abs(nums[j]-axis)):
        nums_.append(nums[i])
        i -= 1
      else:
        nums_.append(nums[j])
        j += 1
      print nums_
    return nums_


if __name__ == "__main__":
  a = Solution()
  print a.sortTransformedArray([-4, -2, 2, 4], 1, 3, 5)
  print a.sortTransformedArray([-4, -2, 2, 4], -1, 3, 5)
  print a.sortTransformedArray([1], -1, 3, 5)
  arr = [-100,-84,-84,-82,-68,-56,-40,-30,48,56,59,73,73,73,87]
  print a.sortTransformedArray(arr, 96, -66, 28)
