"""
163. Missing Ranges (Medium)

Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

"""

class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        n = len(nums)
        if n == 0 or lower > nums[-1] or upper <= nums[0]:
            if lower == upper: return [str(lower)]
            else: return [str(lower) + '->' + str(upper)]
            
        # check first number >= lower
        i, j = 0, n
        while i < j:
            mid = (i + j) / 2
            if nums[mid] == lower:
                i, j = mid, mid
                break
            elif nums[mid] > lower:
                j = mid
            else:
                i = mid + 1
        print i, j, nums[i], nums[j]
        start = i

        # check first number >= upper
        i, j = start, n
        while i < j:
            mid = (i + j) / 2
            if nums[mid] == upper:
                i, j = mid, mid
                break
            elif nums[mid] > upper:
                j = mid
            else:
                i = mid + 1
        end = i
        print end, nums[end]
        # case 1: start == end


if __name__ == "__main__":
    a = Solution()
    print a.findMissingRanges([0, 1, 3, 50, 75], 4, 99)
