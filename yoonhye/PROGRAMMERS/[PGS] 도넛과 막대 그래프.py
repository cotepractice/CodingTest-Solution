def solution(edges):
    N = 1000001
    outgoing = [0 for _ in range(N)]
    ingoing = [0 for _ in range(N)]
    donut, stick, eight = 0, 0, 0

    for x, y in edges:
        outgoing[x] += 1
        ingoing[y] += 1

    for i in range(1, N):
        if outgoing[i] >= 2:
            if ingoing[i] == 0:
                new_node = i
            else:
                eight += 1
        elif outgoing[i] == 0 and ingoing[i] > 0:
            stick += 1
    donut = outgoing[new_node] - stick - eight
    answer = [new_node, donut, stick, eight]

    return answer