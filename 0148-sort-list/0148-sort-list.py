# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         se
class Solution(object):

    def sortList(self, head):
        if head==None or head.next==None:
            return head

        slow=head
        fast=head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        mid=slow.next
        slow.next=None

        left=self.sortList(head)
        right=self.sortList(mid)

        return self.merge(left,right)

    def merge(self,l1,l2):
        dummy=ListNode(0)
        temp=dummy

        while l1 and l2:
            if l1.val < l2.val:
                temp.next=l1
                l1=l1.next
            else:
                temp.next=l2
                l2=l2.next
            temp=temp.next

        if l1:
            temp.next=l1
        else:
            temp.next=l2

        return dummy.next
        