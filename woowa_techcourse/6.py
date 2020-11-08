def solution(logs):
    # {학생번호: [(문제번호, 점수), ...], ...}
    log_table = {}
    for log in logs:
        l = log.split(' ')
        student = l[0]
        question = l[1]
        score = l[2]
        t = (question, score)

        if student in log_table:
            log_table[student].append(t)
        else:
            log_table[student] = [t]

    # 검증 로직
    answer = set()
    for student1, t1 in log_table.items():
        for student2, t2 in log_table.items():

            # 이미 검증한 두 학생 검증 X
            if student1 in answer and student2 in answer:
                continue

            # 같은 학생 검증 X
            if student1 == student2:
                continue

            answer1 = log_table[student1]
            answer2 = log_table[student2]

            # 문제 수 검증
            # 문제 번호, 점수가 같은 답이 5개 이상이면
            # set1 = {s for s in answer1}
            # set2 = {s for s in answer2}
            set1 = set(answer1)
            set2 = set(answer2)
            if 5 <= len(set1.intersection(set2)):
                answer.add(student1)
                answer.add(student2)

    if len(answer) != 0:
        return sorted(list(answer))
    else:
        return ['None']


r = solution(["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90",
              "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"])
print(r)
