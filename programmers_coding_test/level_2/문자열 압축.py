def solution(s):
    answer = len(s)

    for unit in range(1, len(s)):
        result = ''
        count = 1
        for i in range(0, len(s), unit):
            pivot = s[i: i + unit]
            next_pivot = s[i + unit:i + unit + unit]
            if pivot == next_pivot:
                count += 1
            else:
                if 1 < count:
                    result += str(count) + pivot
                else:
                    result += pivot
                count = 1

        if len(result) < answer:
            answer = len(result)
    return answer


r = solution('aabbaccc')
print(r)
