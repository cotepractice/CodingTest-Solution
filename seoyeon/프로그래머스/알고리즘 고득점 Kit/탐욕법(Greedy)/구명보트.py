#프로그래머스 알고리즘 고득점 Kit
#그리디문제
#구명보트

#1.정확성: 14.8, 효율성: 7.4, 합계: 22.2 / 100.0
def solution(people, limit):
    people.sort()
    n = len(people)
    
    #print(people)
    
    cnt = 1     #총 보트의 무게
    boat = 0    #하나의 보트에 포함된 무게
    for i in range(n):
        w = boat + people[i]
        
        if (w <= limit):
            boat += people[i]
            if (i != n-1):
                if (limit-boat<people[i+1]):
                    boat = 0
                    cnt += 1    
                    
                
    return cnt

#2. 정확성: 25.9, 효율성: 11.1, 합계: 37.0 / 100.0
def solution(people, limit):
    people.sort()
    n = len(people)
    
    #print(people)
    
    cnt = 1     #총 보트의 무게
    boat = 0    #하나의 보트에 포함된 무게
    for i in range(n):
        w = boat + people[i]
        
        #다음 인덱스까지했을 때 limit 이하의 경우 같은 cnt와 boat 사용
        if (i < n-1):
            if (w+people[i+1] <= limit):
                continue
        elif (i == n-1):
            continue
        cnt += 1
        boat = 0
                
    return cnt

#3. deque 사용. 정확성: 14.8, 효율성: 7.4, 합계: 22.2 / 100.0
from collections import deque

def solution(people, limit):
    people.sort()
    queue = deque(people)
    #print("queue",queue)
    n = len(people)
    
    cnt = 1     #총 보트의 무게
    boat = 0    #하나의 보트에 포함된 무게
    while True:
        if (queue == deque([])):
            break
        w = queue.popleft()
        if (w+boat <= limit):
            boat = w+boat
        else:
            cnt += 1
            boat = w
                
    return cnt

#4. 정확성: 81.5, 효율성: 18.5, 합계: 100.0 / 100.0
def solution(people, limit):
    people.sort()
    n = len(people)
    
    cnt = 0     #두명이 동시에 타는 보트의 무게
    start = 0
    end = n-1
    while start<end:
        #둘 다 태울 수 있는 경우
        if (people[start]+people[end]<=limit):
            start += 1
            cnt += 1
        #한사람만 태우는 경우
        end -= 1

    answer = n - cnt
                
    return answer