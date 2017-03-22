class Solution(object):
    def twoSum(self, nums, target):
        rec = {} # map num to index
        for i in range(len(nums)):
            # find solution
            if rec.has_key(target-nums[i]):
                return [rec[target-nums[i]], i]
            else:
                rec[nums[i]] = i


if __name__ == '__main__':
  a = Solution()
  print a.twoSum([2,7,11,15], 9)
