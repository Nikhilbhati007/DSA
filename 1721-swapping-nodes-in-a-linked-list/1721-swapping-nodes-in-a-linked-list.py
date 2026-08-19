class Solution(object):
    def swapNodes(self, head, k):
        cnt = 0
        temp = head
        while temp:
            cnt += 1
            temp = temp.next
        t1 = head
        t2 = head
        for i in range(k - 1):
            t1 = t1.next
        for i in range(cnt - k):
            t2 = t2.next
        t1.val, t2.val = t2.val, t1.val
        return head