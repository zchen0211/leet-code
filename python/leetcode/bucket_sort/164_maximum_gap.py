'''
164. Maximum Gap (Hard)

Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Try to solve it in linear time/space.

Return 0 if the array contains less than 2 elements.

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

'''
import collections

class Solution(object):
  def solve2(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n < 2: return 0
    min_ = min(nums)
    max_ = max(nums)
    if min_ == max_: return 0
    # ceil(max_-min_)/(n-1)
    gap = (max_ - min_ + n - 2) / (n-1)
    # n - 1 bucket
    # [0]: [min_, min_+gap)
    # [1]: [min_+gap, min_+2*gap)
    # ...
    # [n-1]: [min_ + (n-1)* gap, max_ + n*gap)
    bucket = []
    for i in range(n):
      bucket.append([])

    # step 1: put in bucket
    for item in nums:
      bucket_id = (item-min_) / gap
      if len(bucket[bucket_id]) == 0:
        bucket[bucket_id] = [item, item]
      else:
        bucket[bucket_id][0] = min(bucket[bucket_id][0], item)
        bucket[bucket_id][1] = max(bucket[bucket_id][1], item)

    print bucket

    # step 2: bucket gap
    result = 0
    last = bucket[0][1]
    for i in range(1, n):
      if len(bucket[i]) > 0:
        result = max(result, bucket[i][0]-last)
        last = bucket[i][1]
    return result


  def maximumGap(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n < 2: return 0
    stat = collections.Counter(nums)

    min_ = min(stat.keys())
    max_ = max(stat.keys())
    curr = min_
    best = 0
    for i in range(min_+1, max_+1):
      if i in stat:
        best = max(best, i-curr)
        curr = i
    return best

  def solve(self, nums):
    n = len(nums)
    if n < 2: return 0
    # decide with / divide
    min_ = min(nums)
    max_ = max(nums)
    divide = 1000
 
    # step 1: divide into [/divide]
    stat = {}
    for i in range(min_/divide, max_/divide+1):
      stat[i] = set()
    for item in nums:
      stat[item/divide].add(item)
    # print 'first bucket: ', stat
    # step 2: solve within bucket
    result = 0
    for i in range(min_/divide, max_/divide+1):
      if len(stat[i]) > 1:
        # print 'solving', i, stat[i]
        tmp_bucket = {}
        for j in range(divide): tmp_bucket[j] = set()
        for item in stat[i]:
          tmp = item % divide
          tmp_bucket[tmp] = set([tmp])
        tmp_result = self.solve_bucket(tmp_bucket, 0, divide-1)
        # print tmp_bucket, tmp_result
        if tmp_result >= 0: result = max(result, tmp_result)
    # print 'solving', stat
    tmp_result = self.solve_bucket(stat, min_/divide, max_/divide)
    # print stat, tmp_result
    if tmp_result >= 0: result = max(result, tmp_result)
    return result

  def solve_bucket(self, bucket, min_, max_):
    result = -1
    found = False
    for i in range(min_, max_+1):
      if len(bucket[i]) > 0:
        if not found:
          found = True
          # last = max(bucket[i])
        else: # already found
          curr = min(bucket[i])
          if result == -1: result = curr - last
          else: result = max(result, curr - last)
        last = max(bucket[i])
    return result


if __name__ == '__main__':
  a = Solution()
  # print a.maximumGap([1,7,2, 15])
  # print a.solve([1,7,2, 15])
  print a.solve2([1,7,2, 15])
  # print a.maximumGap([1,10000000])
  # print a.solve([1,1000])
  print a.solve2([1,1000])
  # print a.solve([1,3,100])
  print a.solve2([1,3,100])
