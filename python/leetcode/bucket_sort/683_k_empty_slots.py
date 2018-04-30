"""
683. K Empty Slots (Hard)

There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.

If there isn't such day, output -1.

Example 1:
Input: 
flowers: [1,3,2]
k: 1
Output: 2
Explanation: In the second day, the first and the third flower have become blooming.
Example 2:
Input: 
flowers: [1,2,3]
k: 1
Output: -1
Note:
The given array will be in the range [1, 20000].
"""

class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        bucket = {} # id_ to (min_, max_)
        n = len(flowers)
        for i in range(n):
            item = flowers[i]
            id_ = item / (k+1)
            if id_ not in bucket or item <= bucket[id_][0]: # can try with small
                if id_-1 in bucket and item-bucket[id_-1][1] == k+1:
                    return i + 1
            if id_ not in bucket or item >= bucket[id_][1]: # can try with small
                if id_+1 in bucket and bucket[id_+1][0] - item == k+1:
                    return i + 1
            # update bucket
            if id_ in bucket:
                min_, max_ = bucket[id_]
                bucket[id_] = (min(min_, item), max(max_, item))
            else:
                bucket[id_] = (item, item)
            print bucket
        return -1

if __name__ == "__main__":
    a = Solution()
    print a.kEmptySlots([1,3,2], 1)
    print a.kEmptySlots([1,2,3], 1)
