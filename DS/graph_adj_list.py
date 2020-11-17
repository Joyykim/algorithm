class Vertex:
    def __init__(self, value, adj_list=None):
        self.value = value
        if adj_list is None:
            adj_list = []
        self.adj_list = adj_list


class Graph:
    def __init__(self):
        self.vertices = []

    def insert(self, value, adj_list):
        self.vertices.append(Vertex(value, adj_list))

    def bfs(self, vert_ind, value):
        visited = []
        queue = [vert_ind]
        while len(queue) != 0:
            curr_ind = queue.pop(0)

            # 이미 방문
            if curr_ind in visited:
                continue

            # 조회
            vertex = self.vertices[curr_ind]
            if vertex == value:
                return True

            # 방문 체크
            visited.append(curr_ind)
            # 큐에 인접 인덱스 추가
            queue += vertex.adj_list
        return False

    def dfs(self, vert_ind, value):
        visited = []

        def search(ind):

            # 버텍스 조회
            if self.vertices[ind].value == value:
                return True

            # 방문 체크
            visited.append(ind)

            # 인접 버텍스들 방문
            for adj_ind in self.vertices[ind].adj_list:
                if adj_ind not in visited:
                    if search(adj_ind):
                        return True
            return False

        return search(vert_ind)
