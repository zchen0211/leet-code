"""
629. K Inverse Pairs Array (Medium)

Given two integers n and k, find how many different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs.

We define an inverse pair as following: For ith and jth element in the array, if i < j and a[i] > a[j] then it's an inverse pair; Otherwise, it's not.

Since the answer may very large, the answer should be modulo 109 + 7.

Example 1:
Input: n = 3, k = 0
Output: 1

Explanation: 
Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pair.

Example 2:
Input: n = 3, k = 1
Output: 2

Explanation: 
The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.

Note:
The integer n is in the range [1, 1000] and k is in the range [0, 1000].
"""

class Solution(object):
  def kInversePairs(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    # Good logic
    # easy to understand
    # but will TLE
    last_ = [1] + [0]*k # 1 num, 0 inverse
    for i in range(2, n+1):
      # tackle [1...i] now
      new_ = [1]
      for j in range(1,k+1):
        # j inverse
        # f(i,j) = f(i-1, j)+...+f(i-1, j-i+1)
        min_ = max(0, j-i+1)
        max_ = j
        new_.append(sum(last_[min_:max_+1]))
      last_, new_ = new_, []
    return last_[-1]

  def solution2(self, n, k):
    MOD = 10**9 + 7
    ds = [0] + [1] * (K + 1)
    for n in xrange(2, N+1):
        new = [0]
        for k in xrange(K+1):
            v = ds[k+1]
            v -= ds[k-n+1] if k >= n else 0
            new.append( (new[-1] + v) % MOD )
        ds = new
    return (ds[K+1] - ds[K]) % MOD

if __name__ == '__main__':
  a = Solution()
  print a.kInversePairs(5, 7)
