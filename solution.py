def solution(arr):
    answer = []
    previous = -1
    for i in arr:
        if i != previous:
            answer.append(i)
            previous = i
    return answer
