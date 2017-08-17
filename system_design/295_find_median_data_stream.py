'''
295. Find Median from Data Stream (Hard)

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples: 
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
'''

class MinHeap(object):
  def __init__(self, cmp=cmp):
    self.nums = []
    self.cnt = 0
    self.cmp = cmp

  def insert(self, num):
    self.nums.append(num)
    self.cnt += 1
    idx = self.cnt - 1
    self.sift_up(idx)

  def pop(self, num=0):
    self.nums[self.cnt-1], self.nums[0] = self.nums[0], self.nums[self.cnt-1]
    ret = self.nums[-1]
    self.nums = self.nums[:-1]
    self.cnt -= 1
    self.sift_down(0)
    return ret

  def sift_up(self, idx):
    # balance all the way up
    while idx>0:
      p_id = (idx-1) / 2
      if self.cmp(self.nums[p_id], self.nums[idx])>0:
        self.nums[p_id], self.nums[idx] = self.nums[idx], self.nums[p_id]
        idx = p_id
      else:
        break

  def sift_down(self, idx):
    while(idx<self.cnt):
      p_idx1 = 2*idx + 1
      p_idx2 = 2*idx + 2
      # print 'ids', idx, p_idx1, p_idx2
      # print self.nums[idx], self.nums[p_idx1], self.nums[p_idx2]
      swap_id, min_ = idx, self.nums[idx]
      if p_idx1 < self.cnt and self.cmp(self.nums[p_idx1], self.nums[idx])<0:
        swap_id, min_ = p_idx1, self.nums[p_idx1]
      if p_idx2 < self.cnt and self.cmp(self.nums[p_idx2], min_)<0:
        swap_id, min_ = p_idx2, self.nums[p_idx2]
      # print 'current, swap', idx, swap_id # , min_
      if swap_id == idx: break
      else:
        self.nums[swap_id], self.nums[idx] = self.nums[idx], self.nums[swap_id]
        idx = swap_id
      # print 'after swapping', self.nums

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_h = MinHeap(cmp= lambda x1, x2: -cmp(x1,x2)) # keep k/2 minimum
        self.min_h = MinHeap()        
        self.cnt = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.max_h.nums) == 0 or num <= self.max_h.nums[0]:
          self.max_h.insert(num)
        else:
          self.min_h.insert(num)
        # balance if required
        if len(self.max_h.nums) < len(self.min_h.nums):
          n = self.min_h.pop()
          self.max_h.insert(n)
        elif len(self.max_h.nums) == len(self.min_h.nums)+2:
          n = self.max_h.pop()
          self.min_h.insert(n)
        self.cnt += 1

    def findMedian(self):
        """
        :rtype: float
        """
        if self.cnt % 2 == 1: return float(self.max_h.nums[0])
        else: return (float(self.max_h.nums[0])+float(self.min_h.nums[0]))/2.


if __name__ == '__main__':
  obj = MedianFinder()
  for i in range(10):
    obj.addNum(i)
    print obj.max_h.nums, obj.min_h.nums
    print obj.findMedian()
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
