import array


class BinaryTree:
    def __init__(self, arr):
        self.array = array.array('l', arr)

    def preorder(self):
        def traversal(i):
            # 노드가 없다면 리턴
            if len(self.array) <= i:
                return

            # 노드 순회
            print(self.array[i])
            # left, right 노드 순회
            traversal(i * 2 + 1)
            traversal(i * 2 + 2)
            return

        traversal(0)
        return

    def inorder(self):
        def traversal(i):
            # 노드가 없다면 리턴
            if len(self.array) <= i:
                return

            # left 순회
            traversal(i * 2 + 1)
            # 노드 순회
            print(self.array[i])
            # right 순회
            traversal(i * 2 + 2)

        traversal(0)
        return

    def postorder(self):
        def traversal(i):
            # 노드가 없다면 리턴
            if len(self.array) <= i:
                return

            # left 순회
            traversal(i * 2 + 1)
            # right 순회
            traversal(i * 2 + 2)
            # 노드 순회
            print(self.array[i])

        traversal(0)
        return

    def bfs(self, value):
        for i in self.array:
            if i == value:
                return True
        return False

    def dfs(self, value):
        def traversal(i):

            # 노드가 없다면 리턴
            if len(self.array) <= i:
                return False

            # 노드 탐색
            if self.array[i] == value:
                return True

            # left, right 노드 탐색
            if traversal(i * 2 + 1) or traversal(i * 2 + 2):
                return True
            else:
                return False

        return traversal(0)


bt = BinaryTree([i for i in range(1, 11)])
# bt.preorder()  # 1 2 4 8 9 5 10 3 6 7
# bt.inorder()  # 8 4 9 2 10 5 1 6 3 7
# bt.postorder()  # 8 9 4 10 5 2 6 7 3 1
# print(bt.bfs(1))
print(bt.dfs(1))
