'''
378. Kth Smallest Element in a Sorted Matrix (Medium)

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 <= k <= n^2.
'''
import Queue

class Solution(object):
  def kthSmallest(self, k, matrix):
    '''
    k: int
    matrix: List[List[int]]
    return int
    '''
    n = len(matrix)
    if n == 0: return

    pq = Queue.PriorityQueue()
    # insert everything from the first row
    for i in range(n):
      # print i
      # print (matrix[0][i], 0, i)
      pq.put((matrix[0][i],0,i))

    for i in range(k):
      x, i, j = pq.get()
      if i+1 != n:
        pq.put((matrix[i+1][j], i+1, j))
    return x


if __name__ == '__main__':
  a = Solution()
  print a.kthSmallest(8, [[ 1,  5,  9],[10, 11, 13],[12, 13, 15]])
