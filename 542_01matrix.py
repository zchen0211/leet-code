'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1: 
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
Example 2: 
Input:

0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1

Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
'''
from collections import deque

class Solution(object):
  def updateMatrix(self, matrix):
    if not matrix or not matrix[0]:
      return [[]]
    h = len(matrix)
    w = len(matrix[0])

    queue = deque()
    queue2 = deque()

    for i in range(h):
      for j in range(w):
        if matrix[i][j] == 1:
          matrix[i][j] = h+w+1
          if i>0 and matrix[i-1][j]==0:
            queue.append([i,j])
            matrix[i][j] = 1
          elif i<h-1 and matrix[i+1][j]==0:
            queue.append([i,j])
            matrix[i][j] = 1
          elif j>0 and matrix[i][j-1]==0:
            queue.append([i,j])
            matrix[i][j] = 1
          elif j<w-1 and matrix[i][j+1]==0:
            queue.append([i,j])
            matrix[i][j] = 1

    step = 1
    while(queue): # not empty
      print 'queue'
      print queue
      while(queue):
        [ti, tj] = queue.popleft()
        if matrix[ti][tj]>step:
          matrix[ti][tj] = step

        # check left, right, up, down visited??
        # if not, enqueue queue2
        if ti>0 and matrix[ti-1][tj]>step:
          queue2.append([i-1,j])
        if ti<h-1 and matrix[ti+1][tj]>step:
          queue2.append([ti+1,tj])
        if tj>0 and matrix[ti][tj-1]>step:
          queue2.append([ti,tj-1])
        if tj<w-1 and matrix[ti][tj+1]>step:
          queue2.append([ti,tj+1])
      print 'matrix'
      print matrix
      # swap queue, queue2, if queue empty
      queue, queue2 = queue2, queue
      step += 1

    return matrix

if __name__ == '__main__':
  a = Solution()
  # print a.updateMatrix([[0,0,0],[0,1,0],[0,0,0]])    
  # print a.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
  # print a.updateMatrix([[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]])
  # print a.updateMatrix([[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]])
  print a.updateMatrix([[1, 0, 1, 1, 0, 0, 1, 0, 0, 1], [0, 1, 1, 0, 1, 0, 1, 0, 1, 1], [0, 0, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 0, 1], [0, 0, 1, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], [1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1, 0, 0, 1, 1]]) 
