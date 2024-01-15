#프로그래머스 알고리즘 고득점 Kit
#해시문제
#전화번호 목록

#1. 정확성 75.0/100.0, 효율성: 0.0/0.0, 합계: 75.0 / 100.0
def solution(phone_book):
    phone_book.sort()
    n = len(phone_book)
    answer = True
    
    dict = {}
    
    for phone in phone_book:
        dict[hash(phone)] = phone
        
    for i in range(n-1):
        for j in range(i+1,n):
            if phone_book[i] in phone_book[j]:
                answer = False
        
    return answer

#2. 정확성: 79.2, 효율성: 8.3, 합계: 87.5 / 100.0
def solution(phone_book):
    phone_book.sort()
    n = len(phone_book)
    answer = True
    
    dict = {}
    
    for phone in phone_book:
        dict[hash(phone)] = phone
        
    for phone1 in dict.values():
        cnt = 0
        char1 = phone1[0]
        for phone2 in dict.values():
            char2 = phone2[0]
            if (char1 != char2):
                continue
            if (phone1 in phone2):
                cnt += 1
                
        if (cnt>=2):
            answer = False            
            break
            
    return answer

#3. 정확성: 83.3, 효율성: 0.0, 합계: 83.3 / 100.0
def solution(phone_book):
    phone_book.sort()
    n = len(phone_book)
    answer = True
    
    dict = {}
    
    for phone in phone_book:
        dict[hash(phone)] = phone

    lst = []
    for i in range(n-1):
        phone1 = dict[hash(phone_book[i])]
        lst = phone_book[i+1:n]
        dict2 = {hash(k):k for k in lst}
        char1 = phone1[0]
        for phone2 in dict2.values():
            char2 = phone2[0]
            if (char1 != char2):
                break
            if (phone1 in phone2):
                answer = False
                break
        
    return answer

#4. 정확성: 83.3, 효율성: 0.0, 합계: 83.3 / 100.0
def solution(phone_book):
    phone_book.sort()
    n = len(phone_book)
    answer = True
    
    dict = {}
    
    for phone in phone_book:
        dict[hash(phone)] = phone

    lst = [0 for _ in range(n)]
    for i in range(n-1):
        phone1 = dict[hash(phone_book[i])]
        #dict2 정의
        lst = phone_book[i+1:n]
        dict2 = {hash(k):k for k in lst}
        m = len(phone1)
        for phone2 in dict2.values():
            m2 = phone2[:m]
            #접두어로 존재하는지 확인
            if (phone1 != m2):
                break
            answer = False
            break
        
    return answer

#5. 정확성: 83.3, 효율성: 16.7, 합계: 100.0 / 100.0

def solution(phone_book):
    dict = {}
    
    for phone in phone_book:
        dict[phone] = 0
    
    answer = True
    
    for phone in phone_book:
        arr = ""
        for n in phone:
            arr += n    #phone_book에서 찾은 문자열을 하나씩 붙여 dict에 존재하는지 확인
            if (arr in dict and arr != phone):
                answer = False
                break
    
    return answer