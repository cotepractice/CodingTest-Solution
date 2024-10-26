#백준 #28278 스택2 구현문제

from collections import deque

global stack
stack = deque()

def one(x):
    stack.append(x)

def two():
    if len(stack) != 0:
        print(stack.pop())
    else:
        print(-1)

def three():
    print(len(stack))

def four():
    if len(stack)==0:
        print(1)
    else:
        print(0)

def five():
    if len(stack) != 0:
        print(stack.pop())
    else:
        print(-1)

N = int(input())

for i in range(N):
    #print("i",i,"stack",stack)
    input_lst = list(map(int,input().split()))

    if input_lst[0] == 1:
        one(input_lst[1])
        continue
    if input_lst[0] == 2:
        two()
        continue
    if input_lst[0] == 3:
        three()
        continue
    if input_lst[0] == 4:
        four()
        continue
    if input_lst[0] == 5:
        five()
        continue