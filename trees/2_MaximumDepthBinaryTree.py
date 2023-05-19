# https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/939516360/

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

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        elif root.left==None and root.right==None:
            return 1
        else:
            return max(1+self.maxDepth(root.left),1+self.maxDepth(root.right))

'''
Runtime: 46 ms
Memory Usage: 16.2 MB
'''

class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        elif root.left==None and root.right==None:
            return 1
        elif root.left!=None and root.right==None:
            return 1+self.maxDepth(root.left)
        elif root.left==None and root.right!=None:
            return 1+self.maxDepth(root.right)
        else:
            return max(1+self.maxDepth(root.left),1+self.maxDepth(root.right))

'''
Runtime: 51 ms
Memory Usage: 16.1 MB
'''     

class Solution3:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

'''
Runtime: 31 ms
Memory Usage: 16.2 MB
'''

# main code
if __name__ == '__main__':
    tree=binaryTree()
    root = tree.insertLevelOrder( [3,9,20,None,None,15,7],0,7)
    obj = Solution()
    a=obj.maxDepth(root)
    print(a)
