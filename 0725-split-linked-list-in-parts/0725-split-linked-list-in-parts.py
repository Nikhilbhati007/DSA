class Solution(object):
    def splitListToParts(self, head, k):
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        size = n // k
        extra = n % k
        ans = []
        temp = head
        for i in range(k):
            part_size = size + (1 if i < extra else 0)
            if part_size == 0:
                ans.append(None)
                continue
            part_head = temp
            for j in range(part_size - 1):
                temp = temp.next
            next_part = temp.next
            temp.next = None
            ans.append(part_head)
            temp = next_part
        return ans