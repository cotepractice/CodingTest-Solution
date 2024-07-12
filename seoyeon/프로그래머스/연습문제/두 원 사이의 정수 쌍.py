#1. 40/100
def solution(r1, r2):
    answer = 0
    
    #x좌표 또는 y좌표가 0인 경우
    answer += (r2-r1+1)*4
    
    #원 내에 존재
    sum = 0
    for x in range(1, r2):
        h2 = (r2**2 - x**2) ** (1/2)
        if x<r1:
            h1 = (r1**2 - x**2) ** (1/2)
            sum += int(h2)-int(h1)
        else:
            sum += int(h2)
    
    answer += sum*4
    #print(sum)
    return answer

#2. 100/100
def solution(r1, r2):
    
    answer,sum = 0,0
    
    #x좌표 또는 y좌표가 0인 경우
    sum += r2-r1+1
    
    #원 내에 존재
    for x in range(1,r2):
        h2 = (r2**2 - x**2) ** 0.5

        if x<r1:
            h1 = (r1**2 - x**2) ** 0.5
            sum += int(h2)-int(h1)
            #반지름으로 r1을 가지는 원이 x가 정수일 때 정수를 지나는 경우
            if float(h1)==float(int(h1)) and h1>0.0:
                sum += 1

        else:
            sum += int(h2)
    
    answer += sum*4

    return answer