#1. 시간 초과. 7.7/100
# from itertools import combinations

# def solution(distance, rocks, n):
#     answer = 0
    
#     choose = list(combinations(rocks,len(rocks)-n))
    
#     for c in choose:
#         min_d = float("inf")
#         c_lst = list(c)
#         c_lst.sort()

#         for i in range(len(c_lst)):
#             if i==0:
#                 min_d = min(min_d,c_lst[i])
#             elif i==len(c_lst):
#                 min_d = min(min_d,distance-c_lst[i])
#             else:
#                 min_d = min(min_d,c_lst[i]-c_lst[i-1])

#         answer = max(answer,min_d)
        
#     return answer

#2. 이분탐색

def solution(distance, rocks, n):
    answer = 0
    
    left,right=0,distance #mid는 최소 거리
    rocks.sort()
    rocks.append(distance)
    
    while left<=right:
        delete_rock=0 #최소 거리를 유지하기 위해 제거해야 하는 바위 수 
        prev_rock=0
        mid = (left+right)//2 #우리가 가정하는 최소 거리
        for r in rocks:
            #현재 바위(r)와 이전의 바위(prev_rock)의 거리가 최소 거리보다 작은 경우 바위 제거
            if r-prev_rock < mid:
                delete_rock += 1
                if delete_rock>n: #바위 개수가 n보다 큰 경우 mid가 작아져야 함
                    break
            else:
                prev_rock=r
        #제거된 바위 개수가 n보다 작거나 같은 경우 mid가 작은 것이므로 최소 거리를 키워야 함
        if delete_rock<=n:
            answer = mid
            left = mid+1
        #제거된 바위 개수가 n보다 큰 경우 mid가 너무 큰 것이므로 줄여야 함   
        else:
            right = mid-1
        
        
    return answer