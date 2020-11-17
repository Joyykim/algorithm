from collections import deque


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, array):
        node_list = [Node(value, None, None) for value in array]
        for ind, node in enumerate(node_list):
            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(node_list):
                node.left = node_list[left]
            if right < len(node_list):
                node.right = node_list[right]

        self.root = node_list[0]

    def preorder(self):
        def traversal(node):
            if node is None:
                return
            print(node.value, end=' ')
            traversal(node.left)
            traversal(node.right)

        traversal(self.root)

    def inorder(self):
        def traversal(node):
            if node is None:
                return
            traversal(node.left)
            print(node.value, end=' ')
            traversal(node.right)

        traversal(self.root)

    def postorder(self):
        def traversal(node):
            if node is None:
                return
            traversal(node.left)
            traversal(node.right)
            print(node.value, end=' ')

        traversal(self.root)

    def bfs(self, value):
        queue = deque()
        queue.append(self.root)
        while len(queue) > 0:
            node = queue.pop()
            if node.value == value:
                return True
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    def dfs(self, value):
        def traversal(node):
            if node is None:
                return False
            if node.value == value:
                return True
            return traversal(node.left) or traversal(node.right)

        return traversal(self.root)


bt = BinaryTree([i for i in range(1, 11)])
print('preorder')
bt.preorder()  # 1 2 4 8 9 5 10 3 6 7
print()
print('inorder')
bt.inorder()  # 8 4 9 2 10 5 1 6 3 7
print()
print('postorder')
bt.postorder()  # 8 9 4 10 5 2 6 7 3 1
print()
print('bfs right', bt.bfs(1))
print('bfs wrong', bt.bfs(11))
print('dfs right', bt.dfs(1))
print('dfs wrong', bt.dfs(11))
