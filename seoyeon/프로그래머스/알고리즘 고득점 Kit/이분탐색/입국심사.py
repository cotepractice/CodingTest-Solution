#1. 테케 6,7,8,9 시간초과
import heapq
def solution(n, times): #n:입국심사인원. times:심사관이 한명을 심사하는데 걸리는 시간 배열
    Q = []
    
    for time in times:
        Q.append([time,time]) #[끝나는 시각,걸리는 시간]
    
    heapq.heapify(Q)
    
    cnt = 0
    while True:
        cnt += 1
        current_time, check_time = heapq.heappop(Q)
        
        if cnt==n:
            answer = current_time
            break
        heapq.heappush(Q,[current_time+check_time,check_time])
    
    return answer