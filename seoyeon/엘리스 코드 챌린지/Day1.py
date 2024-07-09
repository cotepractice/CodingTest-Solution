# 문제

# 목표량
# 시간 제한: 1초
# 엘리스 토끼는 목표량을 정해 수학 문제를 열심히 풉니다. 목표량은 정수입니다.
# 내일 풀 수학 문제의 개수는 오늘 푼 문제 개수의 수와 숫자의 구성이 같으면서, 오늘 푼 문제 개수의 수보다 큰 수 중 가장 작은 수입니다.
# 예를 들어, 오늘 67문제를 풀었으면 다음 날 76문제를 풉니다.
# 오늘 푼 문제의 개수를 줬을 때 다음날 풀 문제의 개수를 출력하는 프로그램을 작성하세요.


# 지시사항
# 입력
# 첫 번째 줄에 오늘 푼 문제의 개수인 자연수 N을 입력합니다.
# 1≤N≤999999
# 정답이 반드시 있는 경우만 입력값으로 주어집니다.
# 출력
# 다음날 풀 문제의 개수를 출력합니다.
# 입력 예시
# 364

# 출력 예시
# 436

#1. 총 점수 100/100
def next_bigger_number(n):
    digits = list(str(n))  # 숫자를 문자열로 변환 후 리스트로 저장
    length = len(digits)

    # 뒤에서부터 탐색하여 처음으로 감소하는 위치를 찾음
    i = length - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    
    # 만약 감소하는 위치가 없다면, 더 큰 수를 만들 수 없으므로 -1을 반환
    if i == -1:
        return -1

    # i 이후에서 i보다 큰 가장 작은 숫자를 찾음
    j = length - 1
    while digits[j] <= digits[i]:
        j -= 1

    # i와 j의 숫자를 교환
    digits[i], digits[j] = digits[j], digits[i]

    # i 이후의 숫자들을 정렬
    digits = digits[:i + 1] + sorted(digits[i + 1:])
    
    # 리스트를 문자열로 변환 후 다시 정수로 변환하여 반환
    return int(''.join(digits))

# 테스트
today_problems = int(input())
tomorrow_problems = next_bigger_number(today_problems)
print(tomorrow_problems)

#2. "다음 순열 알고리즘" 사용

N = list(input())
n = len(N)

i, j = -1,-1
for k in range(n-2,-1,-1):  #뒤에서부터
    #1. pivot 인덱스 찾기. 내림차순이어야하는데, 그렇지 않은 경우의 인덱스 찾기
    if N[k] < N[k+1]:
        i = k
        break

#2. 변경할 인덱스 찾기
for k in range(n-1,i,-1):
    if N[k] > N[i]:
        if j==-1:
            j = k
        else:
            if N[k] < N[j]:
                j = k
#3. 두 인덱스 변경
N[i], N[j] = N[j], N[i]
#4. pivot 인덱스 뒤 오름차순으로 뒤집기
N[i+1:] = N[:i:-1]

print(*N, sep="")