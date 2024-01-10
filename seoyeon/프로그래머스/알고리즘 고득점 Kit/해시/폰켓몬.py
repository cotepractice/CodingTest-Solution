#프로그래머스 알고리즘 고득점 Kit
#해시문제
#폰켓몬

def solution(nums):
    
    dict = {}
    n = len(nums)
    
    answer = 0
    cnt = 0
    for num in nums:
        if (hash(num) not in dict):
            cnt += 1
        dict[hash(num)] = num
        #print(hash(num))
    
    if (cnt>(n//2)):
        answer = n//2
    else:
        answer = cnt

    return answer