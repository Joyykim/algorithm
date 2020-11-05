from collections import Counter


def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]


def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer)[0]
