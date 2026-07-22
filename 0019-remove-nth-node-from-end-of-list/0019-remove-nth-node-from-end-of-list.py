# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        temp=head
        dummy=ListNode(0)
        dummy.next=head
        count=0
        while temp:
            count+=1
            temp=temp.next
        curr=dummy
        for i in range(count-n):
            curr=curr.next
        if curr:
            curr.next=curr.next.next
        return dummy.next

            
        
    