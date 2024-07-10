
#1. 45.8/100
from collections import deque

def solution(plans):
    answer = []
    Q = deque([])   #남아 있는 plan
    
    
    #1. plan 시작 순서로 정렬
    plans.sort(key=lambda x:x[1])
    
    for k in range(len(plans)):
        check = 0
    
        name, start_t, take_t= plans[k]
                
        start_h, start_m = start_t.split(":")
        start_h, start_m, take_t = int(start_h), int(start_m), int(take_t)
        
        end_h = start_h + (start_m+take_t)//60
        end_m = (start_m+take_t)%60
        
        if k!=len(plans)-1:
            next_name, next_t, next_take_t = plans[k+1]
            
            next_h, next_m = next_t.split(":")
            next_h, next_m, next_take_t = int(next_h), int(next_m), int(next_take_t)
            
            #끝낼 수 있는 경우
            if (next_h > end_h) or (next_h==end_h and next_m >= end_m):
                answer.append(name)
                #Q 존재
                if Q != deque([]):
                    #Q 돌리기
                    while check==0:
                        Q_name, Q_take_t = Q.pop()
                        can_take_t = (next_h-end_h)*60 + (next_m-end_m)

                        #Q에서 완료할 수 있는 경우
                        if Q_take_t <= can_take_t:
                            answer.append(name)
                            end_h += Q_take_t//60
                            end_m += Q_take_t%60 

                        #다음 꺼 시작해야 함
                        else:
                            Q_take_t -= can_take_t
                            Q.append([Q_name, Q_take_t])
                            check = 1
                    
            #끝낼 수 없는 경우
            else:
                not_h, not_m = next_h-start_h, next_m-start_m
                take_t -= not_h*60 + not_m 
                Q.append([name,take_t])

        else:
            name, start_t, take_t= plans[k]
            answer.append(name)
                
    #모두 다 돌리고 
    while Q:
        name, take_t = Q.pop()
        answer.append(name)
        
    return answer

#2. 100/100
from collections import deque

def solution(plans):
    #반례1. plans = [["1", "00:00", "30"], ["2", "00:10", "10"], ["3", "00:30", "10"], ["4", "00:50", "10"]]
    answer = []
    Q = deque([])   #남아 있는 plan    
    
    #1. plan 시작 순서로 정렬
    plans.sort(key=lambda x:x[1])
    
    #2. index 0부터 len(plans)-1까지 
    for k in range(len(plans)-1):
    
        name, start_t, take_t= plans[k] 
        #시작 시간    
        start_h, start_m = map(int, start_t.split(":"))
        take_t = int(take_t)
        
        #종료 시간
        end_h = start_h + (start_m+take_t)//60
        end_m = (start_m+take_t)%60
        
        #직후 진행하는 과제 시간
        next_name, next_t, next_take_t = plans[k+1]
            
        next_h, next_m = map(int, next_t.split(":"))
        next_take_t = int(next_take_t)
            
        #a. 끝낼 수 있는 경우
        if (next_h > end_h) or (next_h==end_h and next_m >= end_m):

            answer.append(name)
            #바로 다음 과제를 시작하지 않고 Q 존재
            if not (end_h==next_h and end_m==next_m) and Q != deque([]):
                #Q 돌리기
                for _ in range(len(Q)):
                    Q_name, Q_take_t = Q.pop()
                    can_take_t = (next_h-end_h)*60 + (next_m-end_m)

                    #Q에서 완료할 수 있는 경우
                    if Q_take_t <= can_take_t:
                        answer.append(Q_name)
                        end_h += Q_take_t//60
                        end_m += Q_take_t%60 

                    #다음 꺼 시작해야 함
                    else:
                        Q_take_t -= can_take_t
                        Q.append([Q_name, Q_take_t])
                        break
                    
        #b. 끝낼 수 없는 경우
        else:
            not_h, not_m = next_h-start_h, next_m-start_m
            take_t -= not_h*60 + not_m 
            Q.append([name,take_t])

    #2. 맨 뒤
    name, start_t, take_t= plans[-1]
    answer.append(name)
                
    #모두 다 돌리고 
    while Q:
        name, take_t = Q.pop()
        answer.append(name)
        
    return answer