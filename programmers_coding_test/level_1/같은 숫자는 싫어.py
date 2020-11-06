def solution(arr):
    prev = -1
    answer = []
    for i in arr:
        if i != prev:
            answer.append(i)
            prev = i
    return answer
