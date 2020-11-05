def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    correct = {1: 0, 2: 0, 3: 0}

    for idx, answer in enumerate(answers):
        if answer == s1[idx % len(s1)]:
            correct[1] += 1
        if answer == s2[idx % len(s2)]:
            correct[2] += 1
        if answer == s3[idx % len(s3)]:
            correct[3] += 1

    best = max(correct.values())
    result = []
    for student, score in correct.items():
        if score == best:
            result.append(student)
    return sorted(result)
