#프로그래머스 알고리즘 고득점 Kit 
#정렬문제
#가장 큰 수 

#1. 정확성: 40.0/100.0
#런타임에러 발생
def solution(numbers):
    answer = ''
    
    n = len(numbers)

    str_numbers = []
    for i in range(n):
        number = str(numbers[i])
        str_numbers.append(number)
    
    #정렬
    str_numbers.sort(reverse=True)

    #한 자리수가 맨 뒤로 정렬되는데, 한자리수가 그 앞으로 갈 때 수가 더 커지면 위치 변경
    for k in range(n-1,0,-1):
        if ((str_numbers[k][0] == str_numbers[k-1][0]) and (len(str_numbers[k]) == 1 and int(str_numbers[k-1][1]) < int(str_numbers[k]))):
            str_numbers[k], str_numbers[k-1] = str_numbers[k-1], str_numbers[k]    
    
    #문자열로 결합
    for j in range(n):
        answer += str_numbers[j]
    return answer

#2. 정확성: 40.0/100.0
#런타임에러 X
def solution(numbers):
    answer = ''
    
    n = len(numbers)

    str_numbers = []
    for i in range(n):
        number = str(numbers[i])
        str_numbers.append(number)
    
    #정렬
    str_numbers.sort(reverse=True)

    #한 자리수가 맨 뒤로 정렬되는데, 한자리수가 그 앞으로 갈 때 수가 더 커지면 위치 변경
    for k in range(n-1,0,-1):
        if ((str_numbers[k][0] == str_numbers[k-1][0]) and (len(str_numbers[k]) == 1)):
            tmp1 = ''
            tmp2 = ''
            
            tmp1 += str_numbers[k-1]
            tmp1 += str_numbers[k]
            
            tmp2 += str_numbers[k]
            tmp2 += str_numbers[k-1]
            
            if (int(tmp2) > int(tmp1)):
                str_numbers[k], str_numbers[k-1] = str_numbers[k-1], str_numbers[k]    
    print(str_numbers)
    #문자열로 결합
    for j in range(n):
        answer += str_numbers[j]
    return answer

#3. 정확성: 53.3/100.0
def solution(numbers):
    answer = ''
    
    n = len(numbers)

    str_numbers = []
    for i in range(n):
        number = str(numbers[i])
        str_numbers.append(number)
    
    #정렬
    str_numbers.sort(reverse=True)

    #한 자리수가 맨 뒤로 정렬되는데, 한자리수가 그 앞으로 갈 때 수가 더 커지면 위치 변경
    for k in range(n-1,0,-1):
        tmp1 = ''
        tmp2 = ''
            
        tmp1 += str_numbers[k-1]
        tmp1 += str_numbers[k]
            
        tmp2 += str_numbers[k]
        tmp2 += str_numbers[k-1]
            
        if (int(tmp2) > int(tmp1)):
            str_numbers[k], str_numbers[k-1] = str_numbers[k-1], str_numbers[k]    

    #문자열로 결합
    for j in range(n):
        answer += str_numbers[j]
    return answer

#4. 정확성: 100.0/100.0
def solution(numbers):
    answer = ''
    
    n = len(numbers)

    str_numbers = []
    for i in range(n):
        number = str(numbers[i])
        str_numbers.append(number)
    
    #정렬
    #int 수를 str로 변환한 후 numbers의 원소가 1000이하이므로 모두 3자리수이상으로 만들어 자릿수 맞춰 계산
    str_numbers.sort(key= lambda x:x*3, reverse=True)

    #문자열로 결합
    for j in range(n):
        answer += str_numbers[j]

    #예외처리: [0,0,0,0]과 같이 0으로만 구성된 경우
    answer = int(answer)
    answer = str(answer)
    return answer