# Python3 program to construct binary
# tree from given array in level
# order fashion Tree Node

# Helper function that allocates a
#new node
class newNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class binaryTree:
    # Function to insert nodes in level order
    def insertLevelOrder(self,arr, i, n):
        root = None
        if i < n:
            root = newNode(arr[i])

            root.left = self.insertLevelOrder(arr, 2 * i + 1, n)
            root.right = self.insertLevelOrder(arr, 2 * i + 2, n)
        return root

    # Function to print tree nodes in
    # InOrder fashion
    def inOrder(self,root):
        if root != None:
            self.inOrder(root.left)
            print(root.val,end=" ")
            self.inOrder(root.right)

    def preOrder(self,root):
        if root != None:
            print(root.val,end=" ")
            self.inOrder(root.left)
            self.inOrder(root.right)

    def treeToArr(self,head):
        arr_ans=[]
        arr=[]
        arr.append(head)
        while(len(arr)!=0):
            node=arr.pop(0)
            arr_ans.append(node.val)
            if node.left!=None:
                arr.append(node.left)  
            if node.right!=None:
                arr.append(node.right)
        return arr_ans

# Driver Code
# if __name__ == '__main__':
#     arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
#     n = len(arr)
#     root = None
#     root = insertLevelOrder(arr, 0, n)
#     inOrder(root)

'''
------------------------------------------------
Reference material:
https://www.geeksforgeeks.org/construct-complete-binary-tree-given-array/
------------------------------------------------
'''