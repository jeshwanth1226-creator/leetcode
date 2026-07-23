# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self,head):
        fp=head
        sp=head
        while(fp!=None and fp.next!=None):
            fp=fp.next.next
            sp=sp.next
        return sp