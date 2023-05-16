#https://leetcode.com/problems/same-tree/


from typing import Optional,TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#solution 1
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None:
            return True
        if (p!=None and q==None) or (p==None and q!=None):
            return False
        if (p.left!=None and q.left==None) or (p.left==None and q.left!=None):
            return False
        if p.val!=q.val:
            return False
       
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))


'''
Runtime: 20 ms
Memory Usage: 13.6 MB
------------------------------------------------
'''

#solution 2
class Solution(object):
    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

#solution 3
class Solution:
    def isSameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if b==None and a==None:
            return True
        arr=[]
        arr.extend([a,b])
        while(len(arr)>0):
            q=arr.pop(0)
            p=arr.pop(0)
            if (p!=None and q==None) or (p==None and q!=None):
                return False
            if (p.left!=None and q.left==None) or (p.left==None and q.left!=None):
                return False
            if (p.right!=None and q.right==None) or (p.right==None and q.right!=None):
                return False
            if p.val!=q.val:
                return False
            if(p.left!=None):
                arr.extend([p.left,q.left])
            if(p.right!=None):
                arr.extend([p.right,q.right])
        return True

#solution 4
from collections import deque
class Solution:
    def isSameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if b==None and a==None:
            return True
        arr=deque()
        arr.extend([a,b])
        while(len(arr)>0):
            q=arr.popleft()
            p=arr.popleft()
            if (p!=None and q==None) or (p==None and q!=None):
                return False
            if (p.left!=None and q.left==None) or (p.left==None and q.left!=None):
                return False
            if (p.right!=None and q.right==None) or (p.right==None and q.right!=None):
                return False
            if p.val!=q.val:
                return False
            if(p.left!=None):
                arr.extend([p.left,q.left])
            if(p.right!=None):
                arr.extend([p.right,q.right])
        return True