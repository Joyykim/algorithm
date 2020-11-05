from itertools import combinations


def solution(numbers):
    combi = combinations(numbers, 2)
    return sorted(set(map(lambda x: x[0] + x[1], combi)))
