def solution(n, lost, reserve):
    inter = set(lost).intersection(set(reserve))
    lost = list(set(lost) - inter)
    reserve = list(set(reserve) - inter)
    answer = n - len(lost)
    for re in reserve:
        if re - 1 in lost:
            lost.remove(re - 1)
            answer += 1
        elif re + 1 in lost:
            lost.remove(re + 1)
            answer += 1
    return answer


r = solution(5, [2,4], [1,3,5])

print(r)