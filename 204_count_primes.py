'''
Description:

Count the number of prime numbers less than a non-negative number, n.
'''

import math

class Solution(object):
  # will be out of memory!
  def countPrimes(self, n):
    prime_set = set(range(2,n))
    for i in range(2, int(math.sqrt(n))+1):
      if i in prime_set:
        # remove all i's factor except i itself
        for j in range(2, n/i+1):
          if j*i in prime_set:
            prime_set.remove(j*i)
    return len(prime_set)
  
  def countPrimes2(self, n):
    if n < 3:
      return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
      if primes[i]:
        primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)

if __name__ == '__main__':
  a = Solution()
  print a.countPrimes(100)
