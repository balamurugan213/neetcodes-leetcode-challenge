# https://leetcode.com/problems/invert-binary-tree/
from typing import Optional,TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# solution 1
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root==None:
            return None
        temp= root.right
        root.right=root.left
        root.left=temp

        self.invertTree(root.right)
        self.invertTree(root.left)

        return root

'''
Runtime: 33 ms
Memory Usage: 13.8 MB
------------------------------------------------
'''


# solution 2
class Solution2:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root==None or (root.right==None and root.left==None):
            return root
        temp= root.right
        root.right=root.left
        root.left=temp
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root

'''
Runtime: 31 ms
Memory Usage: 13.9 MB
------------------------------------------------
'''