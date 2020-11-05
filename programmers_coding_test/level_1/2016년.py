from datetime import date


def solution(a, b):
    day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return day[date(2016, a, b).weekday()]


r = solution(5, 24)
print(r)
r = solution(8, 30)
print(r)
