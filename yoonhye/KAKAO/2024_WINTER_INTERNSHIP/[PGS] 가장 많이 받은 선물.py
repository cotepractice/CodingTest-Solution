# 두 사람이 선물을 주고받은 기록이 있다면, 이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 다음달에 선물을 하나 받는다.
# 기록이 없거나 주고받은 수가 같다면, 선물 지수가 더 큰 사람이 더 작은 사람에게 선물을 하나 받는다.
# 선물 지수 : 준 선물의 수 - 받은 선물의 수
# 만약 선물 지수도 같으면 다음 달에 선물을 주고받지 않는다.
# 선물을 가장 많이 받을 친구가 받을 선물의 수
from collections import defaultdict


def solution(friends, gifts):
    scores = defaultdict(int)

    # 선물 주고받은 정보
    info = {}
    for p in friends:
        info[p] = dict.fromkeys(friends, 0)

    for people in gifts:
        a, b = people.split(" ")  # a : 선물 준 사람, b : 선물 받은 사람
        scores[a] += 1
        scores[b] -= 1
        info[a][b] += 1
        info[b][a] -= 1

    result = dict.fromkeys(friends, 0)

    for i in friends:
        for j in friends:
            if i == j:
                continue
            if info[i][j] > 0:  # i가 선물을 더 많이 줬으므로 i가 선물 하나를 받는다.
                result[i] += 1
            elif info[i][j] < 0:  # j가 선물을 더 많이 줬으므로 j가 선물 하나를 받는다.
                result[j] += 1
            else:  # info[i][j] == 0 -> 선물지수 비교
                if scores[i] < scores[j]:  # j의 선물 지수가 더 크기 때문에 b가 선물 하나를 받는다.
                    result[j] += 1
                elif scores[i] > scores[j]:
                    result[i] += 1
    answer = 0
    for p in friends:
        answer = max(answer, result[p])

    return answer//2    #중복되므로 2로 나눠줘야 함
