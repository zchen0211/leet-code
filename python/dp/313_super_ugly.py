'''
313. Super Ugly Number (Medium)

Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k <= 100, 0 < n <= 106, 0 < primes[i] < 1000.
(4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
'''

class Solution(object):
  def nthSuperUglyNumber(self, n, primes):
    if n <= 1: return 1
    prime_num = len(primes)
    b_prime_ind = [0] * prime_num
    
    res = [1]
    cnt = 1
    while(cnt<n):
      b_res = [res[b_prime_ind[i]]*primes[i] for i in range(prime_num)]
      b_res = min(b_res)
      res.append(b_res)
      print b_res
      for j in range(prime_num):
        if b_res == res[b_prime_ind[j]]*primes[j]:
          b_prime_ind[j] += 1
      cnt += 1
    return res[-1]


if __name__ == '__main__':
  a = Solution()
  print a.nthSuperUglyNumber(12, [2,7,13,19])
