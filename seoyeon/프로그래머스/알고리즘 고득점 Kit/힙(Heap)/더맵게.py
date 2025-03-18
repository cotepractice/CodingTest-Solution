# 1.내 코드 
# 정확성: 71.0 (테케 1,3,8,14 실패)
# 효율성: 16.1
# 합계: 87.1 / 100.0
import heapq

def solution(scoville, K):
    answer = 0
    n = len(scoville)
    
    heapq.heapify(scoville) 
    while True:
        
        if scoville[0]>=K:
            break
        if answer>n:
            answer = -1
            break
        answer += 1
                
        x=heapq.heappop(scoville)
        y=heapq.heappop(scoville)
        
        heapq.heappush(scoville,x+2*y)
        
    return answer

#2. 정답
import heapq

def solution(scoville, K):
    answer = 0
    n = len(scoville)
    
    heapq.heapify(scoville) 
    while True:
        
        if scoville[0]>=K:
            break
        if len(scoville)<2: #내 코드와 이 부분 다름
            answer = -1
            break
        answer += 1
                
        x=heapq.heappop(scoville)
        y=heapq.heappop(scoville)
        
        heapq.heappush(scoville,x+2*y)
        
    return answer