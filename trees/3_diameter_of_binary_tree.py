# https://leetcode.com/problems/diameter-of-binary-tree/

'''
Given the root of a binary tree, return the length of the 
diameter of the tree.

The diameter of a binary tree is the length of the longest 
path between any two nodes in a tree. This path may or may 
not pass through the root.
'''

import sys
sys.path.insert(0,".")
from modules.binary_tree import binaryTree
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

# main code
if __name__ == '__main__':
    tree=binaryTree()
    root = tree.insertLevelOrder( [1,2,3,4,5,None,None],0,7)
    obj = Solution()
    a=obj.diameterOfBinaryTree(root)
    print(a)


