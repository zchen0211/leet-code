'''
216. Combination Sum III (Medium)

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
'''


class Solution(object):
  def helper_func(self, k, n, tmp_min):
    # use k nums to for n, each one > tmp_min
    if k == 1:
      if n < 10:
        return [[n]]
      else:
        return []
    elif k == 2:
      return [[i,n-i] for i in range(tmp_min+1,(n+1)/2) if i<n-i and i<9 and n-i<10]
    else:
      # i + k-1, n-1
      result = []
      for i in range(tmp_min+1, n/k):
        # print 'i', i, 'k', k-1, 'n', n-i, 'min', i
        if i<9:
          tmp_result = self.helper_func(k-1, n-i, i)
          for item in tmp_result:
            if max(item)<10:
              result.append([i]+item)
      return result


  def combinationSum3(self, k, n):
    return self.helper_func(k, n, 0)


if __name__ == '__main__':
  a = Solution()
  print a.combinationSum3(3,7)
  print a.combinationSum3(3,9)
