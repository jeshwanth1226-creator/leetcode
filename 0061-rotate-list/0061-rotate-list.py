# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        temp=head
        poi=head
        dummy=ListNode(0)
        prev=None
        Head=poi
        count=0
        while temp:
            count+=1
            temp=temp.next
        if k>=count:
            k%=count
        if k==0:
            return head
        for i in range(count-k-1):
            poi=poi.next
        next=poi.next
        poi.next=prev
        prev=next
        while prev.next:
            prev=prev.next
        dummy.next=next
        prev.next=Head
        return dummy.next
        

