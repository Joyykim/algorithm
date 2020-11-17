class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def put(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
        else:
            node = Node(value, self.tail, None)
            self.tail.next = node
            self.tail = node

    def get(self):
        # 언더플로우
        if self.is_empty():
            return None

        value = self.head.value
        self.head = self.head.next
        self.head.prev = None
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.head.value

    def print(self):
        if self.is_empty():
            print('[]')
        else:
            s = '['
            curr = self.head
            while curr.next is not None:
                s += f'{curr.value}, '
                curr = curr.next
            s += f'{curr.value}]'
            print(s)

    def is_empty(self):
        return self.head is None
