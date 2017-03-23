class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        # empty corner case
        if not findNums:
            return []
        # go through and push to a stack if not decreasing
        stack = []
        next_dic = {}
        for i in range(len(nums)):
            tmp = nums[i]
            while len(stack)>0 and tmp>stack[-1]:
                # not empty and still larger than current
                tmp2 = stack.pop()
                next_dic[tmp2] = tmp
            stack.append(tmp)
        # go through remaining stuff
        while len(stack)>0:
            num = stack.pop()
            next_dic[num] = -1
            
        result = []
        for num in findNums:
            result.append(next_dic[num])
        return result
