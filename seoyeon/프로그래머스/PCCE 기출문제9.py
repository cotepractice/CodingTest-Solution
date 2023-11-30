# [PCCE 기출문제] 9번
# dx,dy 사용. n을 직접 설정해 처리할 것

def solution(board, h, w):
    count = 0
    n = len(board)

    dh = [0,1,-1,0]
    dw = [1,0,0,-1]
    
    for i in range(4):
        h_check = h+dh[i]
        w_check = w+dw[i]
        
        if (0<=h_check<n and 0<=w_check<n):
            if (board[h][w] == board[h_check][w_check]):
                count += 1
        
    answer = count
    return answer