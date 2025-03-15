#프로그래머스 알고리즘 고득점 Kit 
#완전탐색
#카펫

def solution(brown, yellow):
    answer = [] #[가로,세로].가로x 세로y
    
    lst = []
    for i in range(1,brown//2): #세로<=가로. i:세로,j:가로 
        j = brown//2+2-i #x+y = brown//2 + 2
        lst.append([j,i])
    
    for l in lst:
        x,y = l[0],l[1]
        if (x-2) * (y-2) == yellow:
            answer = [x,y]
            return answer
