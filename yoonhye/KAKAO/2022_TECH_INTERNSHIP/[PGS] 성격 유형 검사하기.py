# 하나의 지표에서 각 성격 유형 점수가 같으면, 두 성격 유형 중 사전 순으로 빠른 성격 유형을 검사자의 성격 유형이라고 판단한다.
# 지표 번호 순서대로 return
# 비동의 / 동의
# 사전순으로 더 앞에 있는게 점수를 얻으면 +, 아니면 -
# 1 - 3 / 2 - 2 / 3 - 1 / 4 - 0 / 5 - 1 / 6 - 2 / 7 - 3
# math.ceil(3/x)

import math

def solution(survey, choices):
    answer = ''
    mbti = {"RT": 0, "CF": 0, "JM": 0, "AN": 0}  # 1~4번 지표
    for group, value in zip(survey, choices):
        if (value >= 4):
            value -= 4  # group[1]한테 점수 부여
            if (group[1] > group[0]):  # group[1]이 사전순으로 더 뒤에 있는 경우
                mbti[group[0] + group[1]] -= value
            else:  # group[1]이 사전순으로 더 앞에 있는 경우
                mbti[group[1] + group[0]] += value

        else:  # group[0]한테 점수 부여
            value = math.ceil(3 / value)
            if (group[1] > group[0]):  # group[0]이 사전순으로 더 앞에 있는 경우
                mbti[group[0] + group[1]] += value
            else:  # group[0]이 사전순으로 더 뒤에 있는 경우
                mbti[group[1] + group[0]] -= value

    for key in mbti:
        if mbti[key] < 0:  # 사전순으로 더 뒤에 있는거 출력
            answer += key[1]
        else:  # 사전순으로 더 앞에 있는거 출력
            answer += key[0]

    return answer