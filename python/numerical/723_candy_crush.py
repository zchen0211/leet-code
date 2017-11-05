"""
723. Candy Crush (Medium)

This question is about implementing a basic elimination algorithm for Candy Crush.

Given a 2D integer array board representing the grid of candy, different positive integers board[i][j] represent different types of candies. A value of board[i][j] = 0 represents that the cell at position (i, j) is empty. The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally, "crush" them all at the same time - these positions become empty.
After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. (No new candies will drop outside the top boundary.)
After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.
You need to perform the above rules until the board becomes stable, then return the current board.

Example 1:
Input:
board = 
[[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,2,1,2,2],[4,1,4,4,1014]]
Output:
[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]
Explanation: 

Note:
The length of board will be in the range [3, 50].
The length of board[i] will be in the range [3, 50].
Each board[i][j] will initially start as an integer in the range [1, 2000].
"""

class Solution(object):
  def candyCrush(self, board):
    """
    :type board: List[List[int]]
    :rtype: List[List[int]]
    """
    m = len(board)
    print m
    if m == 0: return board
    n = len(board[0])
    print n
    if m == 0: return board

    id_2_pos = {}
    for i in range(m):
      for j in range(n):
        item = board[i][j]
        if item > 0:
          if item not in id_2_pos:
            id_2_pos[item] = []
          id_2_pos[item].append((i,j))
    print id_2_pos

    flag = True
    while flag:
      # check
      flag = False
      remove_list = []
      for k in id_2_pos.keys():
        print 'key', k
        if len(id_2_pos[k]) == 0:
          remove_list.append(k)
        if len(id_2_pos[k]) < 3:
          continue
        # check horizontal
        ret1 = self.check_horizontal(id_2_pos[k])
        if len(ret1) > 0: flag = True
        print ret1
        # check vertical
        ret2 = self.check_vertical(id_2_pos[k])
        print ret2
        if len(ret2) > 0: flag = True
        # set ret1 and ret2 as zero
        for item in ret1:
          i, j = item
          board[i][j] = 0
        for item in ret2:
          i, j = item
          board[i][j] = 0
      # remove
      for k in remove_list: del id_2_pos[k]
      print board      
      # break 
  
      # if flag, move everything down
      if flag:
        for i in range(n):
          j = m - 1 # valid_id
          jj = m - 1
          while jj >= 0:
            if board[jj][i] == 0: jj -= 1
            else:
              board[j][i] = board[jj][i]
              j, jj = j-1, jj-1
          # set board[0:j][i]
          for k in range(j+1): board[k][i] = 0

        # reset statistics
        id_2_pos = {}
        for i in range(m):
          for j in range(n):
            item = board[i][j]
            if item != 0:
              if item not in id_2_pos: id_2_pos[item] = []
              id_2_pos[item].append((i,j))
        print id_2_pos 
      print 'new board', board      

    return board

  def check_horizontal(self, list_):
    list_.sort()
    print 'hori', list_
    n = len(list_)
    i = 0
    ret = []
    while i < n:
      y, x = list_[i]
      j = i + 1
      while j < n and list_[j][0] == y and list_[j][1]==list_[j-1][1]+1:
        j += 1
      j -= 1
      if j - i >= 2:
        for k in range(i, j+1): ret.append(list_[k])
      i = j + 1
    return ret

  def check_vertical(self, list_):
    list_.sort(key = lambda item: (item[1], item[0]))
    print 'vertical', list_
    n = len(list_)
    i = 0
    ret = []
    while i < n:
      y, x = list_[i]
      j = i + 1
      while j < n and list_[j][1] == x and list_[j][0]==list_[j-1][0]+1:
        j += 1
      j -= 1
      if j - i >= 2:
        for k in range(i, j+1): ret.append(list_[k])
      i = j + 1
    return ret


if __name__ == "__main__":
  a = Solution()
  board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
  a.candyCrush(board)
