class Solution(object):
  def check(self, nums):
    n = len(nums)
    if n <=2 :return True
    cnt = 0
    res = []
    for i in range(n-1):
      if nums[i] > nums[i+1]:
        cnt += 1
        res.append(i)
    print cnt
    if cnt >= 2:
      return False
    if cnt == 0:
     return True

    # cnt == 1 case
    i = res[0]
    print i, nums[i]
    if i == 0: return True
    # check set n[i] = n[i+1]
    elif nums[i+1] >= nums[i-1]: return True
    elif i+1 == n-1: return True
    elif nums[i+2] >= nums[i]: return True
    else: return False


if __name__ == "__main__":
  a = Solution()
  print a.check([4,2,3])
  print a.check([4,2,1])
  print a.check([3,4,2,3])
  print a.check([2,3,3,2,4])
  print a.check([-1,4,2,3])
