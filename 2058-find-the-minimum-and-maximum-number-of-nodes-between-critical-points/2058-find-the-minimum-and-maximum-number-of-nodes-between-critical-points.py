# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        temp=head
        nnode=None
        prev=None
        res=[]
        cnt=0
        while (temp):
            nnode=temp.next
            if nnode is None:
                break
            if prev is None:
                prev=temp
                temp=temp.next
                cnt+=1
                continue
            if (prev.val < temp.val and temp.val > nnode.val) or (prev.val > temp.val and temp.val < nnode.val):
                res.append(cnt)
            prev=temp
            temp=temp.next
            cnt+=1
        n=len(res)
        if n<2:
            return [-1,-1]
        minimum = float('inf')
        for i in range(1, n):
            minimum = min(minimum, res[i] - res[i-1])
        maximum = res[n-1] - res[0]

        return [minimum, maximum]
            
        