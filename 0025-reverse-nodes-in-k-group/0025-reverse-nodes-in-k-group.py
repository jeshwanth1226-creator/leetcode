# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        dummy.next=head
        g_prev=dummy
        while True:
            kth=g_prev
            for i in range(k):
                kth=kth.next
                if kth is None:
                    return dummy.next
            g_next=kth.next
            curr=g_prev.next
            prev=g_next
            while curr!=g_next:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            temp=g_prev.next
            g_prev.next=kth
            g_prev=temp



        

