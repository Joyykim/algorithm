def solution(s):
    i = len(s) // 2
    if len(s) % 2:
        answer = s[i]
    else:
        answer = s[i-1] + s[i]
    return answer


r = solution('abcde')
r = solution('qwer')
print(r)
