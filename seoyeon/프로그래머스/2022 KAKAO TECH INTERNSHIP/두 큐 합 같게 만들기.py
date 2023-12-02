#16:08-16:50, 16:53-15:47

#1. 전체 합을 구해서 하나의 list의 합 구하기
#2. pop과 insert가 동시에 일어나므로 처리 => 맨 앞 요소 제거, 다른 리스트에서 뺀 값 맨 뒤에 붙이기
#3. 예외처리: (1)합이 홀수인 경우 (2)수가 안 만들어지는 경우 -1 return


# 첫번째 코드
# 아래 코드 정확성 90.0 / 100.0, "시간초과" 발생
def solution(queue1, queue2):
    
    sum = 0     # sum, half, queue1_sum 계산
    queue1_sum = 0
    for i in range(len(queue1)):
        sum += queue1[i]
    queue1_sum = sum
    for i in range(len(queue2)):
        sum += queue2[i]
    queue2_sum = sum - queue1_sum
    half = sum // 2
    
    if (sum%2==1):  #예외처리(1)
        return -1

    cnt = 0    
    all = len(queue1) + len(queue2) 
    while (queue1_sum != half):
        if (cnt > all): #예외처리(2)
            return -1
        while (queue1_sum>queue2_sum):
            #이동
            pop1 = queue1[0]
            queue1.pop(0)
            queue2.append(pop1) 
            
            queue1_sum -= pop1
            queue2_sum += pop1
            cnt += 1
        while (queue1_sum<queue2_sum):
            #이동
            pop2 = queue2[0]
            queue2.pop(0)
            queue1.append(pop2) 
            
            queue1_sum += pop2
            queue2_sum -= pop2
            cnt += 1

    return cnt

#두번째 코드

from collections import deque

def solution(queue1, queue2):
    
    # sum, half, queue1_sum 계산
    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)
    total = queue1_sum + queue2_sum

    q1 = deque(queue1)
    q2 = deque(queue2)
    
    if (total%2==1):  #예외처리(1)
        return -1

    cnt = 0    
    all = len(queue1) + len(queue2) 
    while (queue1_sum != queue2_sum):
        if (cnt > all): #예외처리(2)
            return -1
        while (queue1_sum>queue2_sum):
            #이동
            pop1 = q1.popleft()
            q2.append(pop1) 
            
            queue1_sum -= pop1
            queue2_sum += pop1
            cnt += 1
        while (queue1_sum<queue2_sum):
            #이동
            pop2 = q2.popleft()
            q1.append(pop2) 
            
            queue1_sum += pop2
            queue2_sum -= pop2
            cnt += 1

    return cnt