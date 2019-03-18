"""
470. Implement Rand10() Using Rand7() (Medium)

Given a function rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which generates a uniform random integer in the range 1 to 10.

Do NOT use system's Math.random().



Example 1:

Input: 1
Output: [7]
Example 2:

Input: 2
Output: [8,4]
Example 3:

Input: 3
Output: [8,1,10]


Note:

rand7 is predefined.
Each testcase has one argument: n, the number of times that rand10 is called.
"""


# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            i = rand7()
            j = rand7()
            k = (i - 1) * 7 + j  # 1-49
            if k <= 40:  # 1-40
                break
        res = (k - 1) // 4 + 1
        return res
