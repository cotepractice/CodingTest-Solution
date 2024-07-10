from collections import deque

def solution(scores):
    answer = 0
    my_score = scores[0]
    #1. scores에 합이 자신보다 작거나 같은 값들 제외. 카운트할 필요 없음 
    scores = [x for x in scores if sum(x) > scores[0][0] + scores[0][1]]
    #2. scores에는 자신도 제외한 자기보다 큰 값들만 존재하므로 +1 해야함
    answer = len(scores)+1
    #예외: scores의 길이가 0이면 자기자신밖에 없는 것이므로 1 반환
    if len(scores) == 0:
        return 1
    #3. scores 첫 번째 요소는 내림차순, 두 번째 요소는 오름차순 정렬
    scores.sort(key=lambda x:(-x[0],x[1]))

    #예외: 자신이 인센티브 받지 못하는 경우
    for i in range(len(scores)):
        if my_score[0] < scores[i][0] and my_score[1] < scores[i][1]:
            return -1
    
    max_first_number = scores[0][0]
    max_second_number = scores[0][1]
    
    #4. scores 비교
    for k in range(1,len(scores)):
        score1, score2 = scores[k]
        #첫번째 점수가 같은 경우, max_second_number을 더 큰 수로 업데이트(정렬때문에 가능)
        if scores[k] == max_first_number:
            max_second_number = k
            continue
        #첫 번째 점수가 다르고(작고), 
        #두 번째 점수가 max_second_number보다 작은 경우 인센티브 받지 못함
        if score2 < max_second_number:
            answer -= 1
        #max_second_number보다 크거나 같은 경우, max_second_number 업데이트
        #첫 번째 요소와 두 번째 요소 모두 max 값을 구한 후 이후 인덱스 비교
        else:
            max_second_number= score2
    
    return answer