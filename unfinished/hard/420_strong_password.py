"""
420. Strong Password Checker (Hard)

A password is considered strong if below conditions are all met:

It has at least 6 characters and at most 20 characters.
It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.

Insertion, deletion or replace of any one character are all considered as one change.
"""

class Solution(object):
	def solve2(self, s):
		n = len(s)
		deleteTarget = max(0, len(s) - 20)
        act = [0] * 3 # to delete, add, replace
        cond = [1] * 3 # upper, lower and digit
		lenCnt = [{}, {}, {}]

        l = 0
        for r in range(n+1):
        	if r == n or s[l] != s[r]:
            	if r - l > 2:
                    len_ = r - l
                	tmp = lenCnt[len_ % 3]
                    tmp[len_] = tmp.get(len_, 0) + 1
        print lenCnt

    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        cond = [0] * 3
        n = len(s)
        
        stat = [0]
        for i in range(n):
            c = s[i]
            if ord(c) >= ord('a') and ord(c) <= ord('z'):
                cond[0] = 1
            if ord(c) >= ord('A') and ord(c) <= ord('Z'):
                cond[1] = 1        
            if ord(c) >= ord('0') and ord(c) <= ord('9'):
                cond[2] = 1
            if i == 0 or c == s[i-1]: stat[-1] += 1
            else: stat.append(1)
                
        # case 1: already strong
        if n >= 6 and n <= 20:
            change1 = 3 - sum(cond)
            change2 = 0
            for item in stat:
                change2 += item / 3
            return max(change1, change2)
        
        # case 2: < 6
        if n <= 6:
            return max(6 - n, 3 - sum(cond))
        
        # case 3: > 20
        if n > 20:
            new_stat = []
            cut = 0
            result = 0
            change = 3 - sum(cond)
            mod = 0
            for item in stat:
                print item,
                if item <= 2: new_stat.append(item)
                else: # like aaa...
                    cut = item - 2
                    mod += (item - cut) / 3
                    '''
                    if n - cut >= 20:
                        n -= cut
                        result += cut
                    else:
                        cut = n - 20
                        result += cut
                        result += (item - cut) / 3
                        change -= (item - cut) / 3
                        n -= cut
                    '''
                # print result
            # if n > 20: result += n - 20
            # result = max(result, 3 - sum(cond))
            # result += max(0, change)
            result = mod + n - 20
            return result


if __name__ == "__main__":
    a = Solution()
    """
    print a.strongPasswordChecker("a")
    print a.strongPasswordChecker("aaaaaa")
    print a.strongPasswordChecker("aaaaa")
    print a.strongPasswordChecker("aaaa")
    """
    # arr = "abababababababababaaa"
    arr = "aaaabbaaabbaaa123456A"
    print arr, len(arr)
    # print a.strongPasswordChecker(arr)
    print a.solve2(arr)
