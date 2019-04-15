import collections


class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # single list
        single = set([A[0]])
        ari = {} # (end, diff) : length
        for item in A[1:]:
        	# update arith
        	to_remove = []
        	for end, diff in list(ari.keys()):
        		if item - end == diff:
        			ari[item, diff] = ari[end, diff] + 1
        			to_remove.append((end, diff))
        	for e, d in to_remove:
        	 	del ari[(e, d)]
        	# print(item, ari, ari.get((3,0), 0))

        	# with single form ari
        	for item2 in single:
        		if (item, item-item2) not in ari:
        			ari[(item, item-item2)] = 2

        	# add item to single
        	single.add(item)
        return max(ari.values())

    def solve2(self, A):
        dp = collections.defaultdict(int)
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                a, b = A[i], A[j]
                dp[b - a, j] = max(dp[b - a, j], dp[b - a, i] + 1)
        return max(dp.values()) + 1

if __name__ == "__main__":
	a = Solution()
	"""
	print(a.longestArithSeqLength([3,6,9,12]))
	print(a.longestArithSeqLength([9,4,7,2,10]))
	print(a.longestArithSeqLength([20,1,15,3,10,5,8]))
	print(a.longestArithSeqLength([24,13,1,100,0,94,3,0,3]))
	"""
	# print(a.longestArithSeqLength([9,4,7,2,10]))
	print(a.solve2([9,4,7,2,10]))