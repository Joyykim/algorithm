def solution1(phone_book):
    phone_set = set()

    # 길이가 짧은 순으로 정렬
    phone_book.sort(key=len)

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


def solution2(phone_book):
    answer = True

    # 주어진 리스트로 set 생성
    hash_set = set(phone_book)

    # phone_num 하나씩 검사
    for phone_number in phone_book:

        for i in range(1, len(phone_number) + 1):
            # 접두사 = 앞글자부터 하나씩 길이를 늘려가며 slice 한 것
            # ex) "119" > "1", "11", "119"
            prefix = phone_number[:i]

            # 접두사가 set에 있는지(자신 제외 - "119")
            if prefix in hash_set and prefix != phone_number:
                answer = False
    return answer


a = ['119', '976', '11955']
b = ['123', '456', '789']
c = ['12', '123', '1235', '567', '88']

r1 = solution1(a) == False
r2 = solution1(b) == True
r3 = solution1(c) == False

print(r1, r2, r3)
