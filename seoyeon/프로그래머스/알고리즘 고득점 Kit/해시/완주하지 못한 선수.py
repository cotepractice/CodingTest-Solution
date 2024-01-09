#프로그래머스 알고리즘 고득점 Kit
#해시문제
#완주하지 못한 선수

#1. 정확성:58.3, 효율성:0.0, 합계: 58.3/100.0
def solution(participant, completion):
    answer = ''
    for person in participant:
        if person in completion:
            completion.remove(person)
        else:
            answer = person    
    
    return answer

#2. dictionary 사용. 정확성: 41.7, 효율성: 0.0, 합계: 41.7 / 100.0
def solution(participant, completion):
    answer = ''
    #part = {i:0 for i in participant}
    dict = {i:0 for i in completion}

    for part in participant:
        pop_x = dict.pop(part,1)
        print("pop_x",pop_x)
        if (pop_x == 1):    #p가 dict에 존재하면 위에서 정의한 value인 0 출력, 존재하지 않는 경우 기본값인 1 출력
            answer = part
            #print(dict)
            break
    
    return answer

#3. hashmap 사용. hash() 사용
#hash()의 파라미터가 같은 경우 같은 해쉬값을 리턴하지만 같은 인덱스끼리 linkedlist로 되어있어 같은 인덱스가 생길 때마다 노드 추가
def solution(participant, completion):
    dict = {}   #hashmap 구현을 위해 dictionary 자료구조 사용
    
    hashsum = 0 
    for p in participant:
        dict[hash(p)] = p   #hash 함수를 거치면 무작위의 긴 수가 나옴. key는 절대 같지 않고(linked list 사용해 새 노드를 추가해 충돌 방지) value는 같을 수 있음. 현재 key는 hash 값, value는 p
        hashsum += hash(p)
    
    for c in completion:
        hashsum -= hash(c)
        
    return dict[hashsum]