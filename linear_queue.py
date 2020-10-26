import array


class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = array.array('l', [0] * capacity)

    def put(self, value):
        # 오버플로우
        if self.rear == self.capacity:
            return None

        self.array[self.rear] = value
        self.rear += 1

    def get(self):
        # 언더플로우
        if self.front == self.rear:
            return None

        self.front += 1
        return self.array[self.front - 1]

    def peek(self):
        if self.is_empty():
            return None
        return self.array[self.rear - 1]

    def is_empty(self):
        return self.front == self.rear
