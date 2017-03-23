class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
	# sort array
	sorted_nums = [num for num in nums]
	sorted_nums.sort(reverse=True)
	# go through and make a dictionary of ranks
	map_nums_to_id = {}
	for i in range(len(sorted_nums)):
	  map_nums_to_id[sorted_nums[i]] = i+1
	# generate result
	result = []
	for num in nums:
	  rank = map_nums_to_id[num]
	  if rank == 1:
	    result.append('Gold Medal')
	  elif rank == 2:
	    result.append('Silver Medal')
	  elif rank == 3:
	    result.append('Bronze Medal')
	  else:
	    result.append(str(rank))
	return result


if __name__ == '__main__':
  a = Solution()
  print a.findRelativeRanks([10, 3, 8, 9, 4])
