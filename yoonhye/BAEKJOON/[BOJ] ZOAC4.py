from collections import deque

H, W, N, M = map(int, input().split())

one_row_people = (W//(1+M)) + 1 if W%(1+M) != 0 else W//(1+M)
line = (H//(N+1)) + 1 if H % (N+1) != 0 else H//(N+1)

if line == 0:
    line = 1
if one_row_people == 0:
    one_row_people = 1

print(one_row_people * line)