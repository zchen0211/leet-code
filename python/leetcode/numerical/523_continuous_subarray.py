"""
523. Continuous Subarray Sum (Medium)

Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
"""

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        if k == 0:
            for i in range(n-1):
                if nums[i]==0 and nums[i+1]==0:
                    return True
            return False
        if n <= 1: return False
        k = max(k, -k)
        record = set()
        record.add((nums[0]+nums[1])%k)
        if 0 in record: return True
        last = nums[1]%k

        for i in range(2, n):
          item = nums[i]
          if (last+item)%k == 0: return True
          if (k-item) in record: return True
          record_ = set()
          record_.add((last+item)%k)
          for tmp in record:
            record_.add( (item+tmp)%k )
          record = record_
          last = item
        return 0 in record
if __name__ == '__main__':
  a = Solution()
  print a.checkSubarraySum([23,2,6,4,7], 6)
