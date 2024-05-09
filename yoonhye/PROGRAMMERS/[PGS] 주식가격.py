# x초에 들어갔다가 y초에 나오는 방식으로
def solution(prices):
    answer = [0] * len(prices)
    stack = [(0, prices[0])]
    t = 0
    for p in prices[1:]:
        t += 1
        while (stack):
            if p < stack[-1][1]:
                xt, xp = stack.pop()
                answer[xt] = t - xt
            else:
                break
        stack.append((t, p))

    while (stack):
        xt, xp = stack.pop()
        answer[xt] = t - xt

    return answer