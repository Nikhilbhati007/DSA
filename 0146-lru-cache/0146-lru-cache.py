class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove a node from DLL
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # Insert node just before tail
    def insert(self, node):
        prev_node = self.tail.prev

        prev_node.next = node
        node.prev = prev_node

        node.next = self.tail
        self.tail.prev = node

    def get(self, key):

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # This key was recently used
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key, value):

        # Key already exists
        if key in self.cache:

            node = self.cache[key]

            # Update value
            node.value = value

            # Move to MRU
            self.remove(node)
            self.insert(node)

            return

        # New key
        node = Node(key, value)

        self.cache[key] = node
        self.insert(node)

        # Capacity exceeded
        if len(self.cache) > self.capacity:

            # Least recently used node
            lru = self.head.next

            self.remove(lru)
            del self.cache[lru.key]