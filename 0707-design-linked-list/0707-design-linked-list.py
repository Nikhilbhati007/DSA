class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        temp = self.head

        for _ in range(index):
            temp = temp.next

        return temp.val

    def addAtHead(self, val):
        new_node = ListNode(val)

        new_node.next = self.head
        self.head = new_node

        self.size += 1

    def addAtTail(self, val):
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node

        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        new_node = ListNode(val)
        temp = self.head

        for _ in range(index - 1):
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head

            for _ in range(index - 1):
                temp = temp.next

            temp.next = temp.next.next

        self.size -= 1