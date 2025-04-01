from collections import deque
from collections import defaultdict

def solution(priorities, location):
    answer = 0
    
    #location과 비교하기 위해 index와 함께 Q에 삽입
    lst = [[] for _ in range(len(priorities))]
    for i in range(len(priorities)):
        lst[i] = [priorities[i],i]

    Q = deque(lst)
    
    #Q에 존재하는 수와 개수 카운트
    dict = defaultdict(int)
    
    for i in priorities:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
        
    while Q:
        x,idx = Q.popleft()
        #1.x가 Q에서 가장 큰 수인 경우 
        if x==max(dict.keys()):
            #실행되었으므로 순서 1 증가
            answer += 1 
            dict[x] -= 1
            #dict[x]==0인 경우 dict에서 제거
            if dict[x]==0:
                del dict[x]
            #idx==location인 경우 찾고자 했던 값이므로 반복문 종료
            if idx==location:
                break
        #2.그렇지 않은 경우 다시 넣기
        else:
            Q.append([x,idx])
    return answer