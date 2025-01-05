import sys

sys.stdin = open("input.txt", "r")

T = int(input())

def dfs(idx,result):
    global N,lst, num_lst, max, min

    if idx == N-1:
        if result<min:
            min = result
        if result>max:
            max = result
        return

    for i in range(4):
        if lst[i]>0:
            lst[i] -= 1
            if i==0:
                new_result = result + num_lst[idx+1]
            elif i==1:
                new_result = result - num_lst[idx+1]
            elif i==2:
                new_result = result * num_lst[idx+1]
            elif i==3:
                new_result = int(result/num_lst[idx+1])
            dfs(idx+1,new_result)
            lst[i] += 1


for t in range(1,T+1):
    N = int(input())

    lst = list(map(int,input().split())) #N-1개. 1:+,2:-,3:*,4:/인 갯수
    num_lst = list(map(int,input().split())) #N개

    min, max = float("inf"), -float("inf")

    dfs(0,num_lst[0])

    print("#",t,sep="",end=" ")
    print(max-min)