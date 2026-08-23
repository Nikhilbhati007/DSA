
class Solution(object):
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        slow=head
        fast=head
        fast=fast.next.next #skip one step
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        slow.next=slow.next.next
        return head

        