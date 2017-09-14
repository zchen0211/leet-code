"""
655. Print Binary Tree (Medium)

Print a binary tree in an m*n 2D string array following these rules:

The row number m should be equal to the height of the given binary tree.
The column number n should always be an odd number.
The root node's value (in string format) should be put in the exactly middle of the first row it can be put. The column and the row where the root node belongs will separate the rest space into two parts (left-bottom part and right-bottom part). You should print the left subtree in the left-bottom part and print the right subtree in the right-bottom part. The left-bottom part and the right-bottom part should have the same size. Even if one subtree is none while the other is not, you don't need to print anything for the none subtree but still need to leave the space as large as that for the other subtree. However, if two subtrees are none, then you don't need to leave space for both of them.
Each unused space should contain an empty string "".
Print the subtrees following the same rules.
Example 1:
Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]
Example 2:
Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
Example 3:
Input:
      1
     / \
    2   5
   / 
  3 
 / 
4 
Output:

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
Note: The height of binary tree is in the range of [1, 10].
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def helper(self, root):
      # get depth
      if root.left is None and root.right is None:
        return 1
      elif not root.left:
        return self.helper(root.right)+1
      elif not root.right:
        return self.helper(root.left)+1
      else:
        return max(self.helper(root.left), self.helper(root.right)) +1

    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        depth = self.helper(root)
        print depth
        result = self.printHelper(root, depth)
        return result

    def printHelper(self, root, depth_):
        tmp = 2 ** depth_ -1
        if root.left is None and root.right is None:
            result = [[""]*((tmp-1)/2) + [str(root.val)]+ [""]*((tmp-1)/2)]
            return result
            
        if root.left:
            result_l = self.printHelper(root.left, depth_-1)
            print 'left', result_l
       
        if root.right:
            result_r = self.printHelper(root.right, depth_-1)
            print 'right', result_r
        
        # if no left, assign left by duplicate right
        if root.left is None:
            result_l = []
            for sub_list in result_r: # sub_list looks like ["", "1", ""]
                sub_list2 = [""] * len(result_r[0])
                result_l.append(sub_list2)
            print 'left new', result_l
        elif root.right is None:
            result_r = []
            for sub_list in result_l: # sub_list looks like ["", "1", ""]
                sub_list2 = [""] * len(result_l[0])
                result_r.append(sub_list2)
            print 'right new', result_r

        # choose the longest one
        max1_ = max(len(result_l), len(result_r))
        max2_ = max(len(result_l[0]), len(result_r[0]))
        print max1_, max2_
        result = []
        # append a new line first
        sub_list = [""]*max2_+ [str(root.val)] + [""] * max2_
        result.append(sub_list)
        for i in range(max1_):
            sub_list = []
            # result_l
            if i >= len(result_l):
                for j in range(max2_): sub_list.append("")
            else:
                app_ = (max2_ - len(result_l[i])) /2
                for j in range(app_):
                    sub_list.append("")
                for item in result_l[i]:
                    sub_list.append(item)
                for j in range(app_):
                    sub_list.append("")    
            # middle
            sub_list.append("")
            # result_r
            if i >= len(result_r):
                for j in range(max2_): sub_list.append("")
            else:
                app_ = (max2_ - len(result_r[i])) /2
                for j in range(app_):
                    sub_list.append("")
                for item in result_r[i]:
                    sub_list.append(item)
                for j in range(app_):
                    sub_list.append("")
            result.append(sub_list) 
        return result


if __name__ == "__main__":
  a = Solution()
  n1 = TreeNode(1)
  n2 = TreeNode(2)
  n3 = TreeNode(3)
  n4 = TreeNode(4)
  n1.left = n2
  n1.right = n3
  n2.right = n4

  print a.printTree(n1)

