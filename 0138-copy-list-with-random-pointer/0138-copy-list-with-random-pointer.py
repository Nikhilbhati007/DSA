class Node(object):
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        # Step 1: Insert copy nodes
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # Step 2: Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate lists
        curr = head
        dummy = Node(0)
        copy_curr = dummy

        while curr:
            copy = curr.next
            curr.next = copy.next  # restore original

            copy_curr.next = copy
            copy_curr = copy

            curr = curr.next

        return dummy.next