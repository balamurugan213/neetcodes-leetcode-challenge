# https://leetcode.com/problems/invert-binary-tree/
# Difficulty: Easy

#common imports
from typing import Optional
import sys
# tell interpreter where to look
sys.path.insert(0,".")
from modules.binary_tree import binaryTree
import cProfile

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


if __name__ == '__main__':
    tree=binaryTree()
    root = tree.insertLevelOrder([4,2,7,1,3,6,9],0,7)
    obj = Solution()
    a=obj.invertTree(root)
    # tree.preOrder(root)
    # print('\n')
    print(*tree.treeToArr(a))

# print(*printLis(obj.invertTree(root)))

