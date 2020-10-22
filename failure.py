def solution(N, stages):
    failure_dict = {}
    for stage_num in range(1, N + 1):
        reached_players = list(filter(lambda x: stage_num <= x, stages))
        stopped_players = list(filter(lambda x: stage_num == x, stages))
        if len(reached_players) == 0:
            failure_dict[stage_num] = 0
        else:
            failure_dict[stage_num] = len(stopped_players) / len(reached_players)

    answer = sorted(failure_dict, key=lambda x: failure_dict[x], reverse=True)
    return answer


a = solution(132, [2, 1, 2, 6, 2, 21, 23, 64, 13, 97, 53, 98, 31, 12, 87, 76, 24, 90, 12, 122, 128, 100, 3, 3])
print(a)
