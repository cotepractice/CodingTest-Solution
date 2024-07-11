#1. 20/100
def solution(sequence):
    answer = 0
    
    pulse1 = [-1 for _ in range(len(sequence))]
    #누적
    sum1 = [0 for _ in range(len(sequence))]
    sum1_val = 0
    for i in range(len(sequence)):
    
        if i%2==0:
            pulse1[i] = sequence[i]
        else:
            pulse1[i] = sequence[i] * (-1)
        sum1_val += pulse1[i]
        sum1[i] = sum1_val
                
    pulse2 = [-1 for _ in range(len(sequence))]
    sum2 = [0 for _ in range(len(sequence))]
    sum2_val = 0
    for i in range(len(sequence)):
        pulse2[i] = pulse1[i] * (-1) 
        sum2_val += pulse2[i]
        sum2[i] = sum2_val

    if max(sum1) > max(sum2):
        max_idx = sum1.index(max(sum1))
    else:
        max_idx = sum2.index(max(sum2))
    
    answer_lst = [0 for _ in range(max_idx)]
    
    for i in range(max_idx):
        for j in range(i,max_idx+1):
            answer_lst[i] += pulse2[j]
    answer = max(answer_lst)
    
    return answer

#2. 100/100
def solution(sequence):
    answer = 0
    
    dp1 = [0 for _ in range(len(sequence))]
    dp2 = [0 for _ in range(len(sequence))]
    
    dp1[0] = sequence[0]*(-1)
    dp2[0] = sequence[0]
    
    pulse = 1
    for k in range(1,len(sequence)):
        pulse1 = sequence[k] * pulse
        pulse2 = sequence[k] * pulse*(-1)
    
        dp1[k] = max(dp1[k-1]+pulse1, pulse1)
        dp2[k] = max(dp2[k-1]+pulse2, pulse2)
    
        pulse *= (-1)

    answer = max(max(dp1), max(dp2))
    return answer