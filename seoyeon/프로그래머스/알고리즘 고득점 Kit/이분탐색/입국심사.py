#1. 테케 6,7,8,9 시간초과
# import heapq
# def solution(n, times): #n:입국심사인원. times:심사관이 한명을 심사하는데 걸리는 시간 배열
#     Q = []
    
#     for time in times:
#         Q.append([time,time]) #[끝나는 시각,걸리는 시간]
    
#     heapq.heapify(Q)
    
#     cnt = 0
#     while True:
#         cnt += 1
#         current_time, check_time = heapq.heappop(Q)
        
#         if cnt==n:
#             answer = current_time
#             break
#         heapq.heappush(Q,[current_time+check_time,check_time])
    
#     return answer

#2. 이분탐색

def solution(n, times): #n:입국심사인원. times:심사관이 한명을 심사하는데 걸리는 시간 배열
    answer = 0
    left,right = 1, max(times)*n #left,right는 시간. 최대 시간은 가장 오래 걸리는 심사대에서 n명 모두 심사하는 경우
    
    while left<=right:
        mid = (left+right)//2
        people = 0
        for time in times:
            people += mid//time #mid까지의 시간에 심사대가 받을 수 있는 인원수
            if people>=n:
                break
        
        #심사한 사람이 n보다 많은 경우 end 감소
        if people>=n:
            answer = mid
            right = mid-1
        elif people<n:
            left = mid+1
    
    return answer
