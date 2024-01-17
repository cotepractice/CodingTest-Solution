#프로그래머스 알고리즘 고득점 Kit
#그리디문제
#체육복

# #1. 정확성: 90.0, 합계: 90.0 / 100.0
# def solution(n, lost, reserve):
#     answer = 0
    
#     lost.sort()
#     reserve.sort()
    
#     m = len(lost)
    
#     #현재 체육복입은수
#     wear = n-m
    
#     #빌려줄 수 있는 경우
#     lst = []    #이미 빌려준 경우
#     for k in range(len(reserve)):
#         #lost와 reserve 둘 다 속하는 경우
#         if (reserve[k] in lost):
#             lst.append(reserve[k])
#             continue
        
#         #앞뒤둘다 가능한 경우 앞의 번호 학생에게 줘야함 -> 정렬했기때문에
#         if ((reserve[k]-1) in lost and (reserve[k]-1) not in lst): 
#             lst.append(reserve[k]-1)
#             #continue
#         elif ((reserve[k]+1) in lost and (reserve[k]+1) not in lst): 
#             lst.append(reserve[k]+1)
    
#     answer = wear + len(lst)
#     return answer

#2. 

def solution(n, lost, reserve):
    
    lost.sort()
    reserve.sort()
    
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)

    
    for i in reserve:
        if (i-1 in lost):
            lost.remove(i-1)
        elif (i+1 in lost):
            lost.remove(i+1)

    return n-len(lost)


# print(solution(5, [2,4], [1,3,5]))