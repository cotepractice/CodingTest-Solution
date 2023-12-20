#프로그래머스 알고리즘 고득점 Kit 
#완전탐색
#모의고사

def solution(answers):
    sol1 = [1,2,3,4,5]  #5개
    sol2 = [2,1,2,3,2,4,2,5]    #8개
    sol3 = [3,3,1,1,2,2,4,4,5,5]    #10개
    
    n = len(answers)
    
    answer1 = sol1*(n//5 +1)
    answer2 = sol2*(n//8 +1)
    answer3 = sol3*(n//10 +1)
    
    sol = [0,0,0]
    
    for i in range(n):
        if (answers[i] == answer1[i]):
            sol[0] += 1
        if (answers[i] == answer2[i]):
            sol[1] += 1
        if (answers[i] == answer3[i]):
            sol[2] += 1
    
    idx = 0
    answer = []
    for k in range(3):
        if (k == 0):
            answer.append(k+1)
        elif (sol[k] > sol[idx]):
            idx = k
            answer = []
            answer.append(k+1)
        elif (sol[k] == sol[idx]):
            answer.append(k+1)
    
    return answer