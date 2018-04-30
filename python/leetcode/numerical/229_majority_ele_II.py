'''
Given an integer array of size n, find all elements that appear more than n/3 times. The algorithm should run in linear time and in O(1) space.

Show Hint 
'''

class Solution(object):
  def majorityElement(self, nums):
    n = [0, 0, 0]
    c = [0., 0., 0.]
    for item in nums:
      if item in n:
        for j in range(3):
          if item == n[j]:
            c[j] += 1
            break
      else:
        write_flag = True
        for j in range(3):
          c[j] -= 0.5
          if c[j] < 0 and write_flag:
            n[j] = item
            c[j] = 1.
            write_flag = False
      print item, 'n: ', n, 'c: ', c
    # count again to see if n are more than [n/3]
    n = set(n)
    result = []
    for item in n:
      if nums.count(item) > len(nums)/3:
        result.append(item)
    return result


if __name__ == '__main__':
  a = Solution()
  print a.majorityElement([1,1,2,2,3])
