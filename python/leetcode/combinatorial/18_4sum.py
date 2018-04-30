'''
18. 4Sum (Medium)

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n < 4: return []
        mapping = {}

        for i in range(n):
            for j in range(i+1, n):
                tmp = nums[i] + nums[j]
                if tmp not in mapping:
                    mapping[tmp] = []
                mapping[tmp].append((i, j))
                        
        result = []
        visited = set()
        for item in mapping:
            comp = target - item
            if comp in mapping:
                for comb1 in mapping[item]:
                    for comb2 in mapping[comp]:
                        comb = set(comb1 + comb2)
                        if len(comb) == 4:
                            comb = list(comb)
                            tmp_result = [nums[item] for item in comb]
                            tmp_result.sort()
                            if tuple(tmp_result) not in visited:
                                visited.add(tuple(tmp_result))
                                result.append(tmp_result)
        return result


if __name__ == "__main__":
	a = Solution()
	print a.fourSum([1, 0, -1, 0, -2, 2])
