# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if head is None or left==right:
            return head
        poi=None
        curr=head
        i=1
        while i<left:
            poi=curr
            curr=curr.next
            i+=1
        last=curr
        prev=None
        for j in range(right-left+1):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        if poi:
            poi.next=prev
        else:
            head=prev
        last.next=curr
        return head
        
        
        
        


        


        
        




        