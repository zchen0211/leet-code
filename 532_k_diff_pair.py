class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 0 or k<0:
            return 0
        # k != 0 case
        if k != 0:
            result = 0
            nums_set = set(nums)
            for i in nums_set:
                if i+k in nums_set:
                    result += 1
        else:
            nums_dict = {}
            result = 0
            for item in nums:
                if not nums_dict.has_key(item):
                    nums_dict[item] = 1
                else:
                    if nums_dict[item] == 1:
                        result += 1
                    nums_dict[item] += 1
        return result
