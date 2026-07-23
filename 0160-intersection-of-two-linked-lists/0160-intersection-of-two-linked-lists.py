# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        count1=0
        count2=0
        t1=headA
        t2=headB
        pA=headA
        pB=headB
        while t1 is not None:
            count1+=1
            t1=t1.next
        while t2 is not None:
            count2+=1
            t2=t2.next
        if count1>count2:
            skipA=count1-count2
            while skipA:
                pA=pA.next
                skipA-=1
        else:
            skipB=count2-count1
            while skipB:
                pB=pB.next
                skipB-=1
        while pA is not pB:
            pA=pA.next
            pB=pB.next
        return  pA
        
        