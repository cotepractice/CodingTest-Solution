#백준7568 덩치
#구현

n = int(input())

score = [0 for _ in range(n)]
w_lst = []
h_lst = []

for i in range(n):
    w, h = [int,input().split()]
    w_lst.append(w)
    h_lst.append(h)

max_w = w_lst[0]
max_h = h_lst[0]

max_lst = []
min_lst = []
for i in range(1,n):
    if (w_lst[i] >= max_w and h_lst[i] >= max_h):
        max_lst.append(w_lst[i], h_lst[i])
        continue
    if (w_lst[i] <= max_w and h_lst[i] <= max_h):
        min_lst.append(w_lst[i], h_lst[i])
        continue
    
print(max_lst)
print(min_lst)