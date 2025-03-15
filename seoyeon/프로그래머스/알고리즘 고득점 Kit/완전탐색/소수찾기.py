#프로그래머스 알고리즘 고득점 Kit 
#완전탐색
#소수찾기

#1. 정확성 75/100(테케2,11 실패, 테케10 시간초과)
from itertools import permutations

answer = 0

#소수 판별
def solv(n):
    global answer
    
    if n<2:
        return
    if n==2:
        answer += 1
        return
        
    for i in range(3,n-1):
        if n%i==0:
            return
    #print("n:",n)
    answer += 1
    

def solution(numbers):
    global answer
    
    answer = 0
    #1)순서상관있이조합. permutations & INT
    n_lst = []
    for number in numbers:
        n_lst.append(number)
    
    permutations_lst = []
    for k in range(1,len(numbers)+1):
        lst = list(permutations(n_lst,k))
        for l in lst:
            str = ""
            for k in range(len(l)):
                str += l[k]
            permutations_lst.append(int(str))

    #print("permutations:",permutations_lst)
    
    #2)중복 제거. {}
    permutations_set = set(permutations_lst)
    #print("set:",permutations_set)
    
    #3)소수인지 확인
    for n in permutations_set:
        solv(n)
    
    return answer

#2. 100

from itertools import permutations

answer = 0
dp = []

#소수 판별
def solv(max_n):
    global dp
    dp = [False for _ in range(max_n+1)]
    
    dp[0],dp[1]=True,True
    
    #DP로 업데이트
    for i in range(2,max_n):
        if dp[i]==False:
            for j in range(i+i,max_n+1,i):
                dp[j]=True
    
def solution(numbers):
    global answer
    
    answer = 0
    #1)순서상관있이조합. permutations & INT
    n_lst = []
    for number in numbers:
        n_lst.append(number)
    
    permutations_lst = []
    for k in range(1,len(numbers)+1):
        lst = list(permutations(n_lst,k))
        for l in lst:
            str = ""
            for k in range(len(l)):
                str += l[k]
            permutations_lst.append(int(str))
    
    #2)중복 제거. {}
    permutations_set = set(permutations_lst)
    
    #3)소수인지 확인
    max_n = 0
    for n in permutations_set:
        if n>max_n:
            max_n = n
    
    solv(max_n)
    
    for n in permutations_set:
        if dp[n]==False:
            print(n)
            answer += 1
    
    return answer
