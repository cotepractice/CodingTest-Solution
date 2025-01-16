#1952 수영장

# import sys
# sys.stdin = open("input.txt", "r")

def solv(current_month,cost):
    global d,m,ms,y,plans,ans

    if current_month >= 12:
        ans = min(ans,cost)
        return
    
    #1일
    days = plans[current_month]
    solv(current_month+1,cost+d*days)

    #1달
    solv(current_month+1,cost+m)

    #3달
    solv(current_month+3,cost+ms)

    #1년
    solv(current_month+12,cost+y)


T = int(input())

for t in range(1,T+1):
    d,m,ms,y = map(int,input().split())
    plans = list(map(int,input().split()))

    ans = float("inf")
    solv(0,0)

    print("#",t,sep="",end=" ")
    print(ans)