import heapq


def dijkstra(start, graph):
    n = len(graph)
    heap = []
    distances = [float('inf')] * n

    heapq.heappush(heap, (0, start))
    distances[0] = 0

    while heap:

        # 현재 노드
        dist, node = heapq.heappop(heap)

        if distances[node] < dist:
            continue

        adj_list = graph[node]

        # 인접 리스트 순회
        for adj_node, adj_dist in adj_list:
            # 현재 노드 거리 + 인접 노드의 가중치
            new_dist = distances[node] + adj_dist

            # 인접 노드 거리 업데이트
            if new_dist < distances[adj_node]:
                distances[adj_node] = new_dist
                # 인접 노드 push
                heapq.heappush(heap, (new_dist, adj_node))

    return distances


graph = [[(2, 5), (3, 2)],  # (인접노드, 가중치)
         [(3, 5), (4, 3)],
         [(0, 3), (4, 9)],
         [(0, 10), (4, 2)],
         [(2, 13), (1, 3)]]
