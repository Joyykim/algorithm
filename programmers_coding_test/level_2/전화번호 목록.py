def solution(phone_book):
    phone_set = set()

    # 길이가 짧은 순으로 정렬
    phone_book.sort(key=lambda x: len(x))

    # phone_num 하나씩 검사
    for phone_num in phone_book:

        for i in range(1, len(phone_num)):
            # 앞글자부터 하나씩 길이를 늘려가며 slice
            # ex) 119 > 1, 11, 119
            s = phone_num[:i]
            if s in phone_set:
                return False

        # 검사 완료한 수는 set 추가
        phone_set.add(phone_num)
    return True


a = ['119', '97674223', '1195524421']
b = ['123', '456', '789']
c = ['12', '123', '1235', '567', '88']

r1 = solution(a) == False
r2 = solution(b) == True
r3 = solution(c) == False

print(r1, r2, r3)
