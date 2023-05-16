#https://leetcode.com/problems/balanced-binary-tree/submissions/946806575/
# https://leetcode.com/problems/balanced-binary-tree/




from typing import Optional,TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#solution 1
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def fun(root):
            if(root==None):
                return [True,-1]
            if(root.left==None and root.right==None):
                return [True,0]
            else:
                left= fun(root.left)
                right=fun(root.right)
                balanced= left[0] and right[0] and abs(left[1]-right[1])<=1
                return [balanced,1+max(left[1],right[1])]
        ans=fun(root)
        return ans[0]

#solution 2
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def fun(root):
            if(root==None):
                return [True,-1]
            else:
                left= [True,0] if root.left==None else fun(root.left)
                right=[True,0] if root.right==None else fun(root.right)
                balanced= left[0] and right[0] and abs(left[1]-right[1])<=1
                return [balanced,1+max(left[1],right[1])]

        ans=fun(root)
        return ans[0]

'''
Runtime: 52 ms
Memory Usage: 19.3 MB
------------------------------------------------
'''

#solution 3
class Solution(object):
    def isBalanced(self, root):
            
        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
            
        return check(root) != -1