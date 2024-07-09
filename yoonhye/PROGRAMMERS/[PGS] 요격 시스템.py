def solution(targets):
    answer = 1
    targets.sort()
    start, end = targets[0]

    for s, e in targets[1:]:
        if s < end <= e:
            continue
        elif start < s and e < end:
            start, end = s, e
        else:
            start, end = s, e
            answer += 1

    return answer