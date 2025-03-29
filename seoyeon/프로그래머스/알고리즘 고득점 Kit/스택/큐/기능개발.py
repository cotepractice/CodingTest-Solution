#1. 90.0/100
#progress:작업진도 ,speeds:개발속도
# def solution(progresses, speeds):
#     answer = []
    
#     end_time = [0 for _ in range(len(progresses))]
    
#     for i in range(len(progresses)):
#         if (100-progresses[i])//speeds[i]==0:
#             end_time[i]=(100-progresses[i])//speeds[i]
#         else:
#             end_time[i]=(100-progresses[i])//speeds[i] + 1
            
#     visited=[False for _ in range(len(progresses))]
#     for i in range(len(progresses)):
#         if visited[i]==True:
#             continue
#         start = i
#         ans = 1
#         for j in range(i+1,len(progresses)):
#             if end_time[j]<=end_time[start]:
#                 ans += 1
#                 visited[j]=True
#             else:
#                 break
#         answer.append(ans)
        
#     return answer

#2. 100/100
#progress:작업진도 ,speeds:개발속도
def solution(progresses, speeds):
    answer = []
    
    end_time = [0 for _ in range(len(progresses))]
    
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i]==0: #이 부분 수정
            end_time[i]=(100-progresses[i])//speeds[i]
        else:
            end_time[i]=(100-progresses[i])//speeds[i] + 1
    
    visited=[False for _ in range(len(progresses))]
    for i in range(len(progresses)):
        if visited[i]==True:
            continue

        start = i
        ans = 1
        for j in range(i+1,len(progresses)):
            if end_time[j]<=end_time[start]:
                ans += 1
                visited[j]=True
            else:
                break
        answer.append(ans)
        
    return answer