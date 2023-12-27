#프로그래머스 알고리즘 고득점 Kit
#정렬문제
#K번째 수

def solution(array, commands):

    answer = []
    for i in range(len(commands)):
        print("[0]", commands[i][0])
        print("[1]", commands[i][1])
        arr = array[commands[i][0]-1:commands[i][1]]
        arr.sort()
        answer.append(arr[commands[i][2]-1])

    return answer