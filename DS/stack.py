import array


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = 0
        self.array = array.array('l', [0] * capacity)

    def push(self, value):
        # 스택 오버플로우
        if self.capacity == self.top:
            return None

        self.array[self.top] = value
        self.top += 1
        return True

    def pop(self):
        # 스택 언더플로우
        if self.top == 0:
            return None

        self.top -= 1
        result = self.array[self.top]
        return result

    def peek(self):
        if self.is_empty():
            return None
        return self.array[self.top - 1]

    def is_empty(self):
        return self.top == 0


stack = Stack(10)
print(stack.array)
stack.push(4)
stack.push(2)
stack.push(5)
stack.push(6)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
print(stack.push(1))
print(stack.push(1))
print(stack.push(1))
print(stack.array)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.array)
print(stack.peek())
