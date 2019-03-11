"""
1007. Minimum Domino Rotations For Equal Row (Medium)

In a row of dominoes, A[i] and B[i] represent the top and bottom halves of the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same, or all the values in B are the same.

If it cannot be done, return -1.

Example 1:

Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by A and B: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.
Example 2:

Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

Note:

1 <= A[i], B[i] <= 6
2 <= A.length == B.length <= 20000
"""

"""
count existence of 1-6:
case 1. none of them < half, return -1
case 2. one digit i > half
 - check which side has the most
  - swap all digit != i, cnt
  - if can't do, return -1
case 3. one digit i and one digit j == half
"""

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        len_ = len(A)
        stat_A, stat_B = {}, {}
        for item in A:
            stat_A[item] = stat_A.get(item, 0) + 1
        for item in B:
            stat_B[item] = stat_B.get(item, 0) + 1
        # case 1:
        candidates = []
        for i in range(1, 7):
            if stat_A.get(i, 0) + stat_B.get(i, 0) >= len_:
                candidates.append(i)
        if len(candidates) == 0: return -1
        # case 2:
        k = candidates[0]

        def check_swap(A_, B_, k):
            cnt = 0
            for i in range(len_):
                if A_[i] == k:
                    continue
                elif A_[i] != k and B_[i] == k:
                    cnt += 1
                else:
                    return -1
            return cnt

        if stat_A.get(k, 0) >= stat_B.get(k, 0):
            result = check_swap(A, B, k)
        else:
            result = check_swap(B, A, k)
        return result


if __name__ == "__main__":
	a = Solution()
	print(a.minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2]))
	print(a.minDominoRotations([3,5,1,2,3], [3,6,3,3,4]))