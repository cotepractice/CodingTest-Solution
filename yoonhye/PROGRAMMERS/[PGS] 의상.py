from collections import defaultdict

def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield arr[i]
        else:
            for next in combination(arr[i + 1:], r - 1):
                yield arr[i] * next


def solution(clothes):
    answer = 0
    info = defaultdict(int)
    for cloth_name, cloth_type in clothes:
        info[cloth_type] += 1

    values = list(info.values())
    for i in range(1, len(info) + 1):
        answer += sum(combination(values, i))

    return answer