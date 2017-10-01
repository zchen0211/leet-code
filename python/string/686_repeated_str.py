"""
686. Repeated String Match (Easy)
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times ("abcdabcdabcd"), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""

class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        nB = len(B)
        nA = len(A)
        rep = 2 * (nB+nA-1) / nA
        A_ = A * rep
        if A_.find(B) == -1: return -1
        i, j = 1, rep
        while i < j:
          mid = (i + j) / 2
          A_ = A * mid
          print i, j, mid, A_
          if A_.find(B) != -1: j = mid
          else: i = mid + 1
        return i


if __name__ == "__main__":
    a = Solution()
    print a.repeatedStringMatch("abcd", "cdabcdab") 
