class Node:
    def __init__(self, val, next_field=None, previous_field=None):
        self.value = val
        self.next = next_field
        self.prev = previous_field


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def prepend(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
        else:
            node = Node(value, self.head)
            self.head.prev = node
            self.head = node

    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.tail = self.head
        else:
            node = Node(value, self.head)
            self.tail.next = node
            self.head = node
            self.tail = Node(value, None, self.tail)

    def set_head(self, index):
        curr = self.head
        for _ in range(index):
            if curr is None:
                return False
            curr = curr.next
        self.head = curr
        curr.prev = None
        return True

    def access(self, index):
        if self.head is None:
            return False

        curr = self.head
        for _ in range(index):
            if curr is None:
                return False
            curr = curr.next
        return curr.value

    def insert(self, index, value):
        if self.head is None and index > 0:
            return False

        if index == 0:
            self.prepend(value)
            return True

        # index 찾아가기
        curr = self.head
        for _ in range(index):
            if curr is None:
                return False
            curr = curr.next

        # 마지막 노드일 때
        if curr is None:
            node = Node(value, None, self.tail)
            self.tail.next = node
            self.tail = node
        # 중간 노드일 때
        else:
            node = Node(value, curr, curr.prev)
            curr.prev.next = node
            curr.prev = node

        return True

    def remove(self, index):
        # 빈 리스트 -> False
        if self.is_empty():
            return False

        # 인덱스 0이고 원소가 하나였을때
        if index == 0:
            self.head = self.head.next
            self.tail =
            return True

        curr = self.head
        for _ in range(index):
            if curr is None:
                return False
            curr = curr.next

        if curr is None:
            return False

        curr.prev.next = curr.next
        if curr.next is not None:
            curr.next.prev = curr.prev
        else:
            # 삭제하려는 노드가 tail
            self.tail = curr.prev

        return True

    def __str__(self) -> str:
        if self.head is None:
            return '[]'
        curr = self.head
        result = '['
        while curr.next is not None:
            result += f'{curr.value}, '
            curr = curr.next
        result += f'{curr.value}]'
        return result

    def print(self):
        """정방향 프린트"""
        if self.head is None:
            print('[]')
        else:
            curr = self.head
            result = '['
            while curr.next is not None:
                result += f'{curr.value}, '
                curr = curr.next
            result += f'{curr.value}]'
            print(result)

    def reverse_list(self):
        """prev를 타서 리스트화"""
        if self.head is None:
            print('[]')
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next

        result = []
        while curr.prev is not None:
            result.append(curr.value)
            curr = curr.prev
        result.append(curr.value)
        return result


def test_DLL(doubly_linked_list):
    """next, prev 연결이 잘되었는지 테스트"""
    curr = doubly_linked_list.head
    if curr is not None:
        next_list = []
        prev_list = []
        while curr.next is not None:
            next_list.append(curr)
            curr = curr.next

        while curr.prev is not None:
            prev_list.append(curr)
            curr = curr.prev
        print(next_list)
        print(prev_list)


my_list = DoublyLinkedList()
# my_list.print()

for i in range(10):
    my_list.append(i + 1)

# my_list.print()

for i in range(10):
    my_list.prepend(i + 1)

# my_list.print()

value = my_list.access(3)
# print('my_list.access(3) = ' + str(value))

my_list.insert(8, 128)
# my_list.print()

my_list.remove(4)
# my_list.print()

# my_list.set_head(10)
my_list.print()

test_DLL()
