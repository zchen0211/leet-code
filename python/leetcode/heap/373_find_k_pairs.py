'''
373. Find K Pairs with Smallest Sums (Medium)

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3 

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]
'''

"""
min-heap to keep an active set k smallest
"""

class Solution(object):
  def kSmallestPairs(self, nums1, nums2, k):
    '''
    nums1: List[int]
    nums2: List[int]
    k: int
    return: List[List[int]]
    '''
    n1 = len(nums1)
    n2 = len(nums2)
    k = min(k, n1*n2)
    if n1 == 0 or n2 == 0: return []

    sum_rec = {}
    for i in range(n1):
      tmp = nums1[i] + nums2[0]
      if tmp not in sum_rec:
        sum_rec[tmp] = set()
      sum_rec[tmp].add((i,0))

    for i in range(n2):
      tmp = nums1[0] + nums2[i]
      if tmp not in sum_rec:
        sum_rec[tmp] = set()
      sum_rec[tmp].add((0,i))

    visited = set()

    result = []
    result_min = None
    while(len(result)<k):
      tmp_min = min(sum_rec.keys())
      tmp = [item for item in sum_rec[tmp_min]]
      i, j = tmp[0]
      if (i,j) not in visited:
        visited.add((i,j))
        result.append([nums1[i], nums2[j]])
        
        if i+1 <= n1-1:
          tmp_ = nums1[i+1] + nums2[j]
          if tmp_ not in sum_rec: sum_rec[tmp_] = set()
          sum_rec[tmp_].add((i+1, j))
        if j+1 <= n2-1:
          tmp_ = nums1[i] + nums2[j+1]
          if tmp_ not in sum_rec: sum_rec[tmp_] = set()
          sum_rec[tmp_].add((i, j+1))
      
      # update num1_rec by removing and adding new one
      sum_rec[tmp_min].remove((i,j))
      if len(sum_rec[tmp_min]) == 0: del sum_rec[tmp_min]
    return result


if __name__ == '__main__':
  a = Solution()
  # print a.kSmallestPairs([1,7,11], [2,4,6], 3)
  print a.kSmallestPairs([1,1,2], [1,2,3], 10)
  # print a.kSmallestPairs([1,2], [3], 3)
