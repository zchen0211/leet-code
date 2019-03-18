"""
74. Search a 2D Matrix (Medium)

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""


"""
Solution 1: Clean
from right-top or left bottom
O(m+n)
"""

"""
Solution 2:
O(logm+logn)
class Solution {
public:
    bool searchMatrix(vector<vector<int> > &matrix, int target) {
        if(!matrix.size() or !matrix[0].size() or target < matrix[0][0]) return false;
        int m = matrix.size(), n = matrix[0].size(), l = 0, r = m * n, k;
        while(l + 1 < r) {
            k = (l + r) / 2;
            if(matrix[k/n][k%n] <= target) l = k;
            else r = k;
        }
        return matrix[l/n][l%n] == target;
    }
};
My idea is just treat the matrix as an flattened sorted array and do the binary search. The trick is you need to convert you 1D index to 2D index using devide&mod.
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
