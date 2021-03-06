keypad = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),

    4: (1, 0),
    5: (1, 1),
    6: (1, 2),

    7: (2, 0),
    8: (2, 1),
    9: (2, 2),

    '*': (3, 0),
    0: (3, 1),
    '#': (3, 2),
}


def get_distance(start, end):
    x_distance = abs(start[0] - end[0])
    y_distance = abs(start[1] - end[1])
    return x_distance + y_distance


def right_push(answer, i):
    answer += 'R'
    return answer, keypad[i]


def left_push(answer, i):
    answer += 'L'
    return answer, keypad[i]


def solution(numbers, hand):
    answer = ''
    left = keypad['*']
    right = keypad['#']
    for i in numbers:

        # 왼쪽 키패드
        if i in [1, 4, 7]:
            answer, left = left_push(answer, i)

        # 오른쪽 키패드
        elif i in [3, 6, 9]:
            answer, right = right_push(answer, i)

        # 중간 키패드
        elif i in [2, 5, 8, 0]:
            left_dis = get_distance(left, keypad[i])
            right_dis = get_distance(right, keypad[i])

            # 거리가 같을 때 자신의 주 손으로 따라감
            if left_dis == right_dis:
                if hand == 'left':
                    answer, left = left_push(answer, i)
                else:
                    answer, right = right_push(answer, i)
            #
            elif left_dis < right_dis:
                answer, left = left_push(answer, i)
            elif right_dis < left_dis:
                answer, right = right_push(answer, i)
    return answer
