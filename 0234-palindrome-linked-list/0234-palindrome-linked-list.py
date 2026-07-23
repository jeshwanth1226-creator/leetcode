# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        temp =head
        slow=head
        fast=head
        while fast and fast. next:
            slow=slow.next
            fast=fast.next.next
        temp=slow
        prev=None
        while temp:
            next_node=temp.next
            temp. next=prev
            prev=temp
            temp=next_node
        left=head
        right=prev
        while right:
            if left. val!=right.val:
                return False
            left=left.next
            right=right.next
        return True