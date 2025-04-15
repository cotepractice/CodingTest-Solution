#1. 실패
from collections import defaultdict
length = 0
def solv(number,current,idx,small):
    if len(current)==length:
        #print("here")
        #print(current)
        return current
    if idx==len(number):
        #print("here2")
        return
    #print(idx)
    if number[idx] in small and small[number[idx]]>=1:
        small[number[idx]] -= 1
    else:
        current.append(number[idx])
    idx += 1
    return solv(number,current,idx,small)
    
def solution(number, k):
    global length
    length = len(number)-k
    answer = ''
    
    tmp_lst = []
    num_lst = []

    for n in number:
        num_lst.append(int(n))
        tmp_lst.append(int(n))

    num_lst.sort()
    small = defaultdict(int)
    #print("num_lst",num_lst)
    for i in range(k):
        if num_lst[i] in small:
            small[num_lst[i]] += 1
        else:
            small[num_lst[i]] = 1
    #print("small",small)
    ans = []
    ans = solv(tmp_lst,[],0,small)
    #print("ans",ans)
    for i in range(len(ans)):
        answer += str(ans[i])
    return answer

#2.성공
def solution(number, k):
    stack = []
    for n in number:
        #조건 1.stack 내 데이터 존재 2. 뺄 수 있는지 3.현재 값이 이전값보다 큰 경우
        while len(stack)>0 and k>0 and stack[-1]<n:
            stack.pop()
            k -= 1
        stack.append(n)
    
    #마지막까지 뺄 수 있는 경우
    if k>0:
        return "".join(stack[:-k])
    #뺄 수 없으면
    else:
        return "".join(stack)