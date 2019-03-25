"""
1023. Binary String With Substrings Representing 1 To N (Mediums)

Given a binary string S (a string consisting only of '0' and '1's) and a positive integer N, return true if and only if for every integer X from 1 to N, the binary representation of X is a substring of S.

Example 1:

Input: S = "0110", N = 3
Output: true
Example 2:

Input: S = "0110", N = 4
Output: false
 

Note:

1 <= S.length <= 1000
1 <= N <= 10^9
"""


class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        def helper(k):
            # binarize
            result = []
            while k != 0:
                result.append(k % 2)
                k = k // 2
            result = result[::-1]
            result = [str(item) for item in result]
            result = "".join(result)
            return result

        for i in range(1, N+1):
            if i % 2 == 1:
                str_ = helper(i)
                curr = i
                while curr <= N:
                    if S.find(str_) < 0:
                        return False
                    str_ += "0"
                    curr *= 2
        return True


if __name__ == "__main__":
    a = Solution()
    print(a.queryString("0110", 4))