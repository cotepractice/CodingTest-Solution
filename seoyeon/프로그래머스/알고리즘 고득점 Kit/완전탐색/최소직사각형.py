#프로그래머스 알고리즘 고득점 Kit 
#완전탐색
#최소직사각형

#1st: 정확성 90/100
def solution(sizes):
    wallet = [0,0]
    
    for size in sizes:
        #처음
        if (size == sizes[0]):
            wallet[0] = size[0]
            wallet[1] = size[1]
            continue
        #크기 안 늘려도 되는 경우
        if ((size[0]<=wallet[0] and size[1]<=wallet[1]) or (size[0]<=wallet[1] and size[1]<=wallet[0])):
            continue
        #크기 늘리는 경우
        else:
            w1 = wallet[0] - size[0]
            h1 = wallet[1] - size[1]
            if (w1<=0 and h1<=0):
                size1 = w1*h1
            elif (w1<=0 and h1>0):
                size1 = abs(w1)*wallet[1]
            elif (w1>0 and h1<=0):
                size1 = wallet[0]*abs(h1)
            
            w2 = wallet[0] - size[1]
            h2 = wallet[1] - size[0]
            if (w2<=0 and h2<=0):
                size2 = w2*h2
            elif (w2<=0 and h2>0):
                size2 = abs(w2)*wallet[0]
            elif (w2>0 and h2<=0):
                size2 = wallet[1]*abs(h2)
            
            if (size1<size2):
                wallet[0] = max(wallet[0], size[0])
                wallet[1] = max(wallet[1], size[1])
            else:
                wallet[0] = max(wallet[0], size[1])
                wallet[1] = max(wallet[1], size[0])                
        
    answer = wallet[0]*wallet[1]
            
    return answer

#2nd: 상대적으로 작은 수를 w로, 큰 수를 h로 설정한 후 최대값 선택
def solution(sizes):
    w_lst = []
    h_lst = []
    
    for size in sizes:
        w = size[0]
        h = size[1]
        if (h<w):
            w, h = h, w
        w_lst.append(w)
        h_lst.append(h)
        
    answer = max(w_lst) * max(h_lst)
            
    return answer