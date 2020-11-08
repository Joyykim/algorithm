def solution(s, op):

    # 연산자 매직 메소드 매칭
    op_table = {
        '+': '__add__',
        '-': '__sub__',
        '*': '__mul__',
    }
    operation = op_table[op]

    answer = []
    for i in range(len(s) - 1):
        # 순회하여 슬라이싱
        a = int(s[:i + 1])
        b = int(s[i+1:])

        # 연산자 매직 메소드 호출
        result = a.__getattribute__(operation)(b)
        answer.append(result)

    return answer

r = solution('1234', '+')
r = solution('987987', '-')
r = solution('31402', '*')
print(r)