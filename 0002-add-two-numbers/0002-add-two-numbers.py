# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        t1=l1
        t2=l2
        l3=ListNode(-1)
        curr=l3
        carry=0
        while t1 is not None or t2 is not None:
            ans=carry
            if t1 :
                ans+=t1.val
            if t2:
                ans+=t2.val
            nnode=ListNode(ans%10)
            carry=ans//10
            curr.next=nnode
            curr=curr.next
            if t1 :
                t1=t1.next
            if t2:
                t2=t2.next
        if carry:
            nnode=ListNode(carry)
            curr.next=nnode
        return l3.next

        
        