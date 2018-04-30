'''
546. Remove Boxes (Medium)

Given several boxes with different colors represented by different positive numbers. 
You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (composed of k boxes, k >= 1), remove them and get k*k points.
Find the maximum points you can get.

Example 1:
Input:

[1, 3, 2, 2, 2, 3, 4, 3, 1]
Output:
23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----> [1, 3, 3, 3, 1] (1*1=1 points) 
----> [1, 1] (3*3=9 points) 
----> [] (2*2=4 points)
Note: The number of boxes n would not exceed 100.
'''

class Solution(object):
  def removeBoxes(self, boxes):
    """
    :type boxes: List[int]
    :rtype: int
    """
    # re-arrange data
    box_arr = []
    curr_ = boxes[0]
    curr_cnt = 1
    i = 1
    while(i<len(boxes)):
      if boxes[i] == curr_:
        curr_cnt += 1
      else:
        box_arr.append([curr_, curr_cnt])
        curr_ = boxes[i]
        curr_cnt = 1
      i += 1
    box_arr.append([curr_, curr_cnt])
    print box_arr
    result = self.helper(box_arr)
    return result


  def helper(self, box_arr):
    offset, box_arr = self.prune(box_arr)
    # print 'final_offset:', offset
    # print 'final_box:', box_arr
    if len(box_arr) == 0: return offset

    # recursively dfs
    result = 0
    n = len(box_arr)
    print 'working on: ', box_arr, offset 
    for i in range(n):
      print 'remove: ', i, box_arr[i],
      # remove item box_arr[i]
      new_box_arr = []
      for j in range(i):
        b_id, b_n = box_arr[j]
        new_box_arr.append([b_id,b_n])
      
      b_id, b_n = box_arr[i]

      new_offset1 = b_n ** 2
      if i>0 and i+1 < n and box_arr[i+1][0] == new_box_arr[-1][0]:
        new_box_arr[-1][1] += box_arr[i+1][1]
        for j in range(i+2, n):
          new_box_arr.append(box_arr[j])
      else:
        for j in range(i+1, n):
          new_box_arr.append(box_arr[j])
      print 'after remove, ', new_box_arr
      # prune
      new_offset2, new_box_arr = self.prune(new_box_arr)
      # recursively helper
      if len(new_box_arr) > 0:
        new_offset3 = self.helper(new_box_arr)
      else:
        new_offset3 = 0
      print new_offset1, new_offset2, new_offset3
      # get max
      result = max(result, new_offset1+new_offset2+new_offset3)
    return offset+result


  def prune(self, box_arr):
    # return offset and new box_arr after pruning

    # one-step pruning: remove all 1-time result
    # statistics of box_arr
    offset = 0
    stat = {}
    for item in box_arr:
      b_id, b_n = item
      if b_id not in stat: stat[b_id] = 1
      else: stat[b_id] += 1
    new_box_arr = []
    for item in box_arr:
      b_id, b_n = item
      # print b_id, b_n, stat[b_id]
      if stat[b_id]>1:
        if len(new_box_arr)==0 or new_box_arr[-1][0]!=b_id:
          new_box_arr.append([b_id, b_n])
        else:
          new_box_arr[-1][1] += b_n
          stat[b_id] -= 1
      else:
        offset += b_n ** 2
        del stat[b_id]
      # print new_box_arr, offset
    # print stat, new_box_arr
    # corner case: empty, or not reducible
    if len(new_box_arr) == 0 or min(stat.values()) >= 2:
      return offset, new_box_arr
    else:
      # otherwise: recursively pruning
      new_offset, new_box_arr = self.prune(new_box_arr)
      return offset+new_offset, new_box_arr

  def solution2(self, boxes):
    n = len(boxes)
    # create n * n * n box
    matrix = []
    for i in range(n):
      tmp1 = []
      for j in range(n):
        tmp2 = [0] * n
        tmp1.append(tmp2)
      matrix.append(tmp1)
    return self.dfs(boxes, matrix, 0, n-1, 0)

  def dfs(self, boxes, matrix, l, r, k):
    if l>r: return 0
    if matrix[l][r][k] != 0:
      return matrix[l][r][k]

    while(r>l and boxes[r]==boxes[r-1]):
      r -= 1
      k += 1
    matrix[l][r][k] = self.dfs(boxes, matrix, l, r-1,0) + (k+1)*(k+1)
    for i in range(l, r):
      if boxes[i] == boxes[r]:
        matrix[l][r][k] = max(matrix[l][r][k], self.dfs(boxes,matrix,l,i,k+1)+self.dfs(boxes,matrix,i+1,r-1,0))
    return matrix[l][r][k]

if __name__ == '__main__':
  a = Solution()
  # print a.removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1])
  # print a.removeBoxes([2, 2, 3, 3, 3, 2, 2, 3, 3, 1])
  # print a.solution2([2, 2, 3, 3, 3, 2, 2, 3, 3, 1])
  print a.solution2([1,2,1])
