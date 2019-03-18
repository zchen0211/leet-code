"""
575. Distribute Candies (Easy)

Given an integer array with even length, where different numbers in this array represent different kinds of candies. Each number means one candy of the corresponding kind. You need to distribute these candies equally in number to brother and sister. Return the maximum number of kinds of candies the sister could gain.

Example 1:
Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
The sister has three different kinds of candies. 
Example 2:
Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1]. 
The sister has two different kinds of candies, the brother has only one kind of candies. 
Note:

The length of the given array is in range [2, 10,000], and will be even.
The number in given array is in range [-100,000, 100,000].
"""
import collections


class Solution(object):
    def distCandies(self, candies):
        """
    :type candies: List[int]
    :rtype: int
    """
        # AC, my original solution
        n = len(candies)
        if n == 0:
            return 0
        record = {}
        if c in candies:
            if c in record:
                record[c] += 1
            else:
                record[c] = 1

        if len(record.keys()) >= n / 2:
            return n / 2
        else:
            return len(record.keys())

    def solution2(self, candies):
        # AC, shorter but slower
        n = len(candies)
        if n == 0:
            return 0
        record = dict(collections.Counter(candies))
        kind = len(record.keys())
        return min(kind, n / 2)
