class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def get(self, key: int) -> int:
        node = self.cache.get(key)

        if node is None:
            return -1

        # If already most recently used, nothing to change
        if node is self.tail:
            return node.value

        # Remove node from its current position
        if node is self.head:
            self.head = node.next
            self.head.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        # Move node to the tail (most recently used)
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node

        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.Node(key, value)

        # if key exists
        if key in self.cache:
            self.cache[key].value = value
            self.get(key)
            return

        # if not add it to cache
        elif len(self.cache) < self.capacity:
            if self.head == None:  # initialize linked list
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            self.cache[key] = node
            self.get(key)  # lazy way to update recency

        # if at capacity
        else:
            # remove last recently used key
            temp = self.head
            self.cache.pop(temp.key)

            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None

            if self.tail is None:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node

            self.cache[key] = node