def get_distance(a, b, n):
    if a > b:
        a, b = b, a
    way1 = abs(a - b)
    way2 = (n - 1 - b) + a + 1
    short = min(way1, way2)
    return short


def solution(n, board):
    table = {}
    for y, sub_list in enumerate(board):
        for x, number in enumerate(sub_list):
            table[number] = (x, y)

    current = [0, 0]
    answer = 0

    for i in range(1, (n ** 2) + 1):
        # i의 칸을 알아내기
        location = table[i]

        # 좌우 방향 결정
        answer += get_distance(current[0], location[0], n)

        # 상하 방향 결정
        answer += get_distance(current[1], location[1], n)

        # 엔터
        answer += 1

        # 커서 이동
        current = location

    return answer


r = solution(4, [[11, 9, 8, 12], [2, 15, 4, 14], [1, 10, 16, 3], [13, 7, 5, 6]])
print(r)
