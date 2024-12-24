T = int(input())  # 테스트케이스 개수 입력

def count_burger(idx, selected):

    global not_m, ans

    # 모든 재료를 확인한 경우
    if idx > N:
        ans += 1
        return

    # 현재 재료를 선택하지 않는 경우
    count_burger(idx + 1, selected)

    # 현재 재료를 선택하는 경우
    for s in selected:
        if not_m[idx][s]:  # 궁합이 맞지 않는 경우 선택하지 않음
            return

    # 현재 재료를 선택하고 다음 단계로 진행
    selected.append(idx)
    count_burger(idx + 1, selected)
    selected.pop()  # 백트래킹

for t in range(1, T + 1):
    # 입력 처리
    N, M = map(int, input().split())  # N: 재료 개수, M: 제약 조건 개수
    not_m = [[False for _ in range(N + 1)] for _ in range(N + 1)]  # 궁합이 맞지 않는 정보

    # 제약 조건 입력
    for _ in range(M):
        a, b = map(int, input().split())
        not_m[a][b] = True
        not_m[b][a] = True

    ans = 0
    count_burger(1, [])  # 재료 1번부터 탐색 시작
    print(f"#{t} {ans}")