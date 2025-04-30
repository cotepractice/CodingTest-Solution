#백준 #15989 1,2,3 더하기 4

#1.Greedy. 시간초과
T = int(input())

for _ in range(T):
    N = int(input())
    ans = 0

    sum = N
    n3 = sum//3+1
    
    for i in range(n3):
        sum = N-3*i
        n2 = (sum//2)+1
        for j in range(n2):
            sum2 = sum- j*2
            if sum2>=0:
                ans += 1

    print(ans)
