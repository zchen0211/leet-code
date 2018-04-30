"""
560. Subarray Sum Equals K (Medium)

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = [0]
        for item in nums:
            res.append(res[-1] + item)
                    
        record = {0: 1}
        result = 0
        for item in res[1:]:
            if item - k in record:
                result += 1
            record[item] = record.get(item, 0) + 1
        return result


if __name__ == "__main__":
    a = Solution()
    print a.subarraySum([1,2,1,2,1], 3)
