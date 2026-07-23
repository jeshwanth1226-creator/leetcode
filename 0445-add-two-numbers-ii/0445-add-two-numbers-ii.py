# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        t1=l1
        t2=l2
        stack1=[]
        stack2=[]
        carry=0
        head=None
        dummy=ListNode(0)
        prev=dummy
        while t1:
            stack1.append(t1.val)
            t1=t1.next
        while t2:
            stack2.append(t2.val)
            t2=t2.next
        while stack1 or stack2 or carry:
            x=stack1.pop() if stack1 else 0
            y=stack2.pop() if stack2 else 0
            total=x+y+carry
            carry=total//10
            digit=total%10
            new_node=ListNode(digit)
            new_node.next=head
            head=new_node
        return head
            

        