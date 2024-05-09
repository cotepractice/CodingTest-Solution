from collections import defaultdict

def solution(clothes):
    answer = 1
    info = defaultdict(int)
    for cloth_name, cloth_type in clothes:
        info[cloth_type] += 1

    for v in info.values():
        answer *= (v + 1)
    answer -= 1

    return answer