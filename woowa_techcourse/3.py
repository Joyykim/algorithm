def solution(money, expected, actual):
    bet = 100
    for e, a in zip(expected, actual):
        if e == a:
            money += bet
            bet = 100
        else:
            money -= bet

            # 파산 - 게임 종료
            if money == 0:
                return 0

            # 베팅금 두배
            bet *= 2

            # 돈 부족 - 남은 금액만 베팅
            if money < bet:
                bet = money

    return money


r = solution(1000, ['H', 'T', 'H', 'T', 'H', 'T', 'H'], ['T', 'T', 'H', 'H', 'T', 'T', 'H'])
r = solution(1200, ['T', 'T', 'H', 'H', 'H'], ['H', 'H', 'T', 'H', 'T'])
print(r)
