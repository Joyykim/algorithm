class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def prepend(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        new_node = Node(value, None)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current is not None:
                current = current.next
            current.next = new_node

    def set_head(self, index):
        current = self.head
        for _ in range(index):
            if current is None:
                raise ValueError
            current = current.next
        self.head = current

    def access(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                raise ValueError
            current = current.next
        return current.value

    def insert(self, index, value):
        if self.head is None and index > 0:
            return False

        if index == 0:
            self.prepend(value)
            return True

        curr = self.head
        prev = None
        for _ in range(index):
            if curr is None:
                return False
            prev = curr
            curr = curr.next

        prev.next = Node(value, curr)
        return True

    def remove(self, index):
        if index == 0:
            if self.head is not None:
                self.head = self.head.next
                return True
            else:
                return False

        curr = self.head
        prev = None
        for _ in range(index):
            if curr is None:
                return False
            prev = curr
            curr = curr.next

        if curr is None:
            return False

        prev.next = curr.next
        return True

    def print(self):
        pass
