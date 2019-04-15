# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        l = S.split("-")
        l2 = [(0, int(S[0]))]
        counter = 1
        for item in l[1:]:
        	if item != "":
        		l2.append([counter, int(item)])
        		counter = 1
        	else:
        		counter += 1
        print(l2)
        root = self.helper(l2)
        return root

    def helper(self, sublist):
    	if len(sublist) == 1:
    		return TreeNode(sublist[0][1])
    	root = TreeNode(sublist[0][1])
    	# go through and split
    	st = []
    	for idx in range(1, len(sublist)):
    		sublist[idx][0] -= 1
    		if sublist[idx][0] == 0:
    			st.append(idx)
    	if len(st) == 1:
    		node = self.helper(sublist[1:])
    	else:
        	node = self.helper(sublist[1:st[1]])
    	root.left = node

    	if len(st) == 2:
       	    node = self.helper(sublist[st[1]:])
    	    root.right = node
    	return root


if __name__ == "__main__":
	a = Solution()
	print(a.recoverFromPreorder("1-2--3--4-5--6--7"))
	print(a.recoverFromPreorder("1-2--3---4-5--6---7"))
