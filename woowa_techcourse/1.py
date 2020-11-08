def solution(grades, weights, threshold):
    grade_weight = {
        'A+': 10,
        'A0': 9,
        'B+': 8,
        'B0': 7,
        'C+': 6,
        'C0': 5,
        'D+': 4,
        'D0': 3,
        'F': 0
    }

    score = 0
    for grade, weight in zip(grades, weights):
        score = score + (grade_weight[grade] * weight)

    answer = score - threshold
    return answer


r = solution(["A+", "D+", "F", "C0"], [2, 5, 10, 3], 50)
r = solution(["B+", "A0", "C+"], [6, 7, 8], 200)
print(r)
