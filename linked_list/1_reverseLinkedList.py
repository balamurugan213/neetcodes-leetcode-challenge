from typing import Optional,ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head==None:
                return head
        lis=head
        nextLis=head.next
        while(nextLis!=None):
            if lis==head:
                lis.next=None
            temp=nextLis.next
            nextLis.next=lis
            lis=nextLis
            nextLis=temp

        self.printLis(lis)
        return lis
    
    def printLis(self,head):
        while(head!=None):
            print(head.val,"-->")
            head=head.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head==None:
                return head
        lis=head
        nextLis=head.next
        while(nextLis!=None):
            if lis==head:
                lis.next=None

            temp=nextLis.next
            nextLis.next=lis

            lis=nextLis
            nextLis=temp
            
        return lis
    
    # def printLis(self,head):
    #     while(head!=None):
    #         print(head.val,"-->")
    #         head=head.next