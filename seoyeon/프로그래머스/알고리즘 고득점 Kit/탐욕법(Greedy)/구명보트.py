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

