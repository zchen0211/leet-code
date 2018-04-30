'''
17. Letter Combinations of a Phone Number (Medium)

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping = {'1': [], '2': ['a','b','c'], '3': ['d','e','f'],
                   '4': ['g','h','i'], '5': ['j','k','l'], '6': ['m','n','o'],
                   '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x','y','z'],
                   '*': ['+'], '0': [' '], '#': []}
        if '1' in digits: return ['']
        result = [""]
        n = len(digits)
        if n == 0: return []
        for i in range(n):
            c = digits[i]
            new_result = []
            c_list = mapping[c]
            for item in result:
                for c_ in c_list:
                    new_result.append(item + c_)
            result, new_result = new_result, []
        return result

