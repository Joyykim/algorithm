import array


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.is_full = False
        self.array = array.array('l', [0] * capacity)

    def put(self, value):
        # 오버플로우
        if self.is_full:
            return None

        self.array[self.rear] = value

        # rear 증가
        self.rear = (self.rear + 1) % self.capacity

        if self.front == self.rear:
            self.is_full = True

    def get(self):
        # 언더플로우
        if not self.is_full and self.front == self.rear:
            return None

        self.is_full = False

        value = self.array[self.front]
        # front 증가
        self.front = (self.front + 1) % self.capacity
        return value

    def peek(self):
        if self.front == self.rear:
            return None
        return self.array[self.front]

    def print(self):
        if self.rear == self.front and self.is_full is False:
            print('[]')
            return

        start = self.front
        end = self.rear
        if self.rear <= self.front:
            end += self.capacity

        s = '['
        for i in range(start, end):
            s += str(self.array[i % self.capacity]) + ' '
        s += ']'
        print(s)


cq = CircularQueue(4)
cq.put(1)
cq.put(1)
cq.put(1)
cq.put(1)
cq.print()
