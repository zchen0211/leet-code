'''
37. Sudoku Solver (Hard)

Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        pts = []
        for i in range(9):
          for j in range(9):
            if board[i][j] == '.':
              pts.append((i,j))
        self.solve(board, pts, 0)
        print board

    def solve(self, board, pts, k):
      # solve k's number
      if k == len(pts):
        print board
        return True

      # enumerate
      flag = [True] * 10
      i, j = pts[k]
      for ii in range(9):
        if board[ii][j] != '.':
          tmp = int(board[ii][j])
          flag[tmp] = False
      for jj in range(9):
        if board[i][jj] != '.':
          tmp = int(board[i][jj])
          flag[tmp] = False

      sub_i, sub_j = i/3, j/3
      for ii in range(sub_i*3, sub_i*3+3):
        for jj in range(sub_j*3, sub_j*3+3):
          if board[ii][jj] != '.':
            tmp = int(board[ii][jj])
            flag[tmp] = False
      print i, j, flag

      solved = False
      for item in range(1, 10):
        if flag[item]:
          # board[i][j] = str(item)
          board[i] = board[i][:j] + str(item) + board[i][j+1:]
          solved = self.solve(board, pts, k+1)
          
        if not solved: # board[i][j] = '.'
          board[i] = board[i][:j] + '.' + board[i][j+1:]
        else:
          return True
      return False


if __name__ == "__main__":
    a = Solution()
    a.solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])
