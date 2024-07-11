# 41.2/100
def solution(sequence, k):
    answer = []
    dif_min = float("inf")
    
    for p in range(len(sequence)-1,-1,-1):
        sum = sequence[p]
        if sum == k:
            answer = [p,p]
            break
            
        for l in range(p-1,-1,-1):
            sum += sequence[l]

            if sum > k:
                break
            elif sum == k:
                if p-l <= dif_min:
                    dif_min = p-l
                    answer = [l,p]
                break
    
    
    return answer

#2. 100/100
def solution(sequence, k):
    answer = [-1,-1]
    dict = {0:-1}   #key가 0~해당 index까지의 합, value가 index. 초기 dict[0]=-1은 첫 인덱스부터 시작하는 경우
    
    sum = 0
    for i in range(len(sequence)):
        sum += sequence[i]
        dict[sum] = i
        
        if (sum-k) in dict:

            if answer==[-1,-1]:
                answer = [dict[sum-k]+1, i]
                continue

            if answer[1]-answer[0] != i-dict[sum-k]-1:
                answer = [dict[sum-k]+1, i] #시작 인덱스, 종료 인덱스

    return answer
