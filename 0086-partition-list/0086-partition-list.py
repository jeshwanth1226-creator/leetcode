
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        temp = head
        d1 = ListNode(0)
        d2 = ListNode(0)
        small = d1
        big = d2
        while temp:
            if temp.val < x:
                small.next = temp
                small = small.next
            else:
                big.next = temp
                big = big.next

            temp = temp.next

        big.next = None
        small.next = d2.next

        return d1.next