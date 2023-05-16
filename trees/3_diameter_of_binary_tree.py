# https://leetcode.com/problems/diameter-of-binary-tree/


###

'''
Given the root of a binary tree, return the length of the 
diameter of the tree.

The diameter of a binary tree is the length of the longest 
path between any two nodes in a tree. This path may or may 
not pass through the root.
'''

from typing import Optional,TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#solution 1
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=[0]
        def dfs(root):
            if not root:
                return -1
            left=dfs(root.left)
            right=dfs(root.right)
            res[0]=max(res[0],2+left+right)
            return 1+max(left,right)
        dfs(root)
        return res[0]

'''
Runtime: 63 ms
Memory Usage: 18.7 MB
------------------------------------------------
'''

#solution 2
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=[0]
        def dfs(root):
            left=dfs(root.left) if root.left!=None else 0
            right=dfs(root.right) if root.right!=None else 0
            res[0]=max(res[0],left+right)
            return 1+max(left,right)
        dfs(root)
        return res[0]

'''
Runtime: 42 ms
Memory Usage: 18.7 MB
------------------------------------------------
'''

'''
Learnings:

Adding few extra conditions in the code can reduce the runtime.
Here I have added check for left and right child if they are None or not - instead of going to None node checking if it is None or not.
SO we avoid going to some nodes which are None and hence reduce the runtime.

using a function inside a function is a good way to avoid using global variables.
'''



