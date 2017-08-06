"""
654. Maximum Binary Tree (Medium)

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
Note:
The size of the given array will be in the range [1,1000].
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        root = self.helper(nums, 0, len(nums)-1)
        return root
        
    def helper(self, nums, i, j):
        if i > j: return None
        # corner case
        if i == j:
            root = TreeNode(nums[i])
            return root
        if i == j-1:
            nodei = TreeNode(nums[i])
            nodej = TreeNode(nums[j])
            if nums[i] > nums[j]:
                nodei.right = nodej
                return nodei
            else:
                nodej.left = nodei
                return nodej
        # find max
        max_i_, max_ = i, nums[i]
        i_ = i+1
        while i_ <= j:
            if nums[i_] > max_:
                max_i_, max_ = i_, nums[i_]
            i_ += 1
            
        root = TreeNode(nums[max_i_])
        root.left = self.helper(nums, i, max_i_-1)
        root.right = self.helper(nums, max_i_+1, j)
        return root

if __name__ == "__main__":
  a = Solution()
  print a.constructMaximumBinaryTree([3,2,1])
