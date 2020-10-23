import array


class ArrayList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.array = array.array('l', [0] * capacity)

    def make_new_arr(self):
        return array.array('l', [0] * self.capacity)

    def is_empty(self):
        return self.length == 0

    def prepend(self, value):
        if self.length == self.capacity:
            # capacity 증가
            self.capacity *= 2
            # 새로운 배열 생성
            new_arr = self.make_new_arr()
            # 값 하나씩 복사
            for i in range(self.length):
                new_arr[i + 1] = self.array[i]
        else:
            # 새로운 배열 생성
            new_arr = self.make_new_arr()
            # 뒤로 한칸씩 밀기
            for i in range(self.length - 1, -1, -1):
                new_arr[i + 1] = self.array[i]
        self.array = new_arr
        self.array[0] = value
        self.length += 1

    def append(self, value):
        if self.length == self.capacity:
            # capacity 증가
            self.capacity *= 2
            # 새로운 배열 생성
            new_arr = self.make_new_arr()
            # 값 하나씩 복사
            for i in range(self.length):
                new_arr[i] = self.array[i]
            self.array = new_arr
        else:
            # 마지막 비어있는 자리에 대입
            self.array[self.length] = value
        self.length += 1

    def set_head(self, index):
        self.capacity -= index
        self.length -= index
        self.array = self.array[index:]

    def access(self, index):
        # 없는 인덱스에 접근시 에러
        if index >= self.length:
            raise ValueError
        return self.array[index]

    def insert(self, index, value):
        if self.length == self.capacity:
            # capacity 증가
            self.capacity *= 2
            # 새로운 배열 생성
            new_arr = self.make_new_arr()
            # 값 하나씩 복사
            for i in range(index):
                new_arr[i] = self.array[i]
            for i in range(index, self.length):
                self.array = new_arr
        else:
            # 마지막 원소부터 하나씩 뒤로 미루기
            for i in range(self.length - 1, index, -1):
                self.array[i] = self.array[i - 1]
        # 비어있는 index 위치에 삽입
        self.array[index] = value
        self.length += 1

    def remove(self, index):
        # 없는 인덱스에 접근시 에러
        if index >= self.length:
            raise ValueError
        # index 위치부터 하나씩 뒤의 원소로 덮어쓰기
        for i in range(index + 1, self.length):
            self.array[i - 1] = self.array[i]
        # array 마지막 자리에 남은 값은 쓰지 못하도록 length 줄이기
        self.length -= 1

    def print(self):
        print(self)

    def __str__(self):
        s = '['
        for i in range(self.length):
            s += str(self.array[i])
            s += ' '
        s += ']'
        return s


my_list = ArrayList(8)
assert my_list.__str__() == '[]'

for i in range(10):
    my_list.append(i + 1)
my_list.print()

for i in range(10):
    my_list.prepend(i + 1)
my_list.print()

print('my_list.access(3) =', my_list.access(3))

my_list.insert(8, 128)
my_list.print()

my_list.remove(4)
my_list.print()

my_list.set_head(10)
my_list.print()
