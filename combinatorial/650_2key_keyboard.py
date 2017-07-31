class Solution(object):
  def minSteps(self, n):
    res = 0
    a, flag = self.is_prime(n)
    print a, flag
    while not flag:
      while n%a == 0:
        res += a
        n /= a
      a, flag = self.is_prime(n)
      print a, flag
    print n, res
    if n != 1:
      res += n
    return res
    
  def is_prime(self, n):
    i = 2
    while i*i <= n:
      if n%i==0 and i!=n:
        return (i, False)
      i += 1
    return (1, True)


if __name__ == '__main__':
  a = Solution()
  # print a.is_prime(9)
  print a.minSteps(5)
