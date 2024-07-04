#프로그래머스

#1 정확도 25/100
from collections import deque

def solution(coin, cards):

    pocket = []
    pair_pocket = []    #둘 다 pocket에 있는 카드쌍. 순서 상관 X. 카드 낼 때 사용
    N = len(cards)
    cards_Q = deque(cards)
    pair = {}   #dictionary. 반드시 가져와야 하는 카드 쌍. 순서 상관 O
    round = 0
    
    
    #1. 처음 카드 뭉치에서 n/3개 뽑기
    plus = 0    #카드 뭉치에서 겹치는 경우 
    for _ in range(N//3):
        card = cards_Q.popleft()
        pocket.append(card)
        #이미 존재하는 경우
        if pair.get(card)!=None or pair.get(N-card+1)!=None:
            if coin-N//3 >= 0:
                plus += 1
            pair_pocket.append([card,N-card+1])
            continue
        
        if card <=N//2:
            pair[card] = N-card+1
        else:
            pair[N-card+1] = card
    
    #2. 
    while True:
        round += 1
        #종결조건1.카드 뭉치가 없는 경우
        if cards_Q == deque([]):
            break
            
        card1 = cards_Q.popleft()
        card2 = cards_Q.popleft()
        
        #2. 넣을지 말지
        #넣는 경우: 기존 pocket의 쌍
        #print("card1",card1,"card2",card2)
        #print('coin',coin)
        if pair.get(card1)!=None or pair.get(N-card1+1)!=None:
            pocket.append(card1)
            pair_pocket.append([card1,N-card1+1])   
                
            coin -= 1
        #더 뽑을 수 있는 경우, 앞에서 뽑기
        #넣는 경우: pocket에 쌍이 있어서 더 뽑을 수 있음
        else:
            if plus > 0:
                pocket.append(card1)
                
                if card1 <=N//2:
                    pair[card1] = N-card1+1
                else:
                    pair[N-card1+1] = card1
                plus -= 1
                coin -= 1

        if coin >= 1:
            if pair.get(card2)!=None or pair.get(N-card2+1)!=None:
                pocket.append(card2)
                pair_pocket.append([card2,N-card2+1])
                
                coin -= 1
        
        #더 뽑을 수 있는 경우, 앞에서 뽑기
        #넣는 경우: pocket에 쌍이 있어서 더 뽑을 수 있음
        else:
            if plus > 0:
                pocket.append(card2)
                #pair_pocket.append([card2,N-card2+1])
                if card2 <=N//2:
                    pair[card2] = N-card2+1
                else:
                    pair[N-card2+1] = card2
                plus -= 1
                coin -= 1
        #print('coin',coin)
        #예외. pocket에 제출할 카드가 없는 경우
        if len(pair_pocket) == 0 and coin >=2:
            if card1 + card2 == N+1:
                pocket.append(card1)
                pocket.append(card2)
                pair_pocket.append([card1,N-card1+1])
                if card1<card2:
                    pair[card1] = card2
                else:
                    pair[card2] = card1
                coin -= 2
        
        #print("pocket1",pocket)
        #print("pair",pair)
        #print("pair_pocket",pair_pocket)
        
        
        #종결조건3.낼 수 있는 카드가 없는 경우
        if len(pair_pocket) == 0:
            break
        else:
            #3. pocket에서 N+1이 되는 카드쌍 제출
            del pair_pocket[0]
        
    
    
    return round

#2 정확도 45/100
from collections import deque

def choose(card1,card2,pocket,pair,pair_pocket,coin):
        global N,plus
        check1, check2 = 0,0
        #2. 넣을지 말지
        #넣는 경우: 기존 pocket의 쌍
        if pair.get(card1)!=None or pair.get(N-card1+1)!=None:
            pocket.append(card1)
            pair_pocket.append([card1,N-card1+1])
            check1 = 1
            coin -= 1
        
        if coin >= 1 and (pair.get(card2)!=None or pair.get(N-card2+1)!=None):
            pocket.append(card2)
            pair_pocket.append([card2,N-card2+1])
            check2 = 1
            coin -= 1    
        
        #더 뽑을 수 있는 경우, 앞에서 뽑기
        #넣는 경우: pocket에 쌍이 있어서 더 뽑을 수 있음    
        if coin>=1 and check1==0 and plus>0:
            pocket.append(card1)
            
            if card1 <=N//2:
                pair[card1] = N-card1+1
            else:
                pair[N-card1+1] = card1
            plus -= 1
            coin -= 1
        
        if coin>=1 and check2==0 and plus>0:
            pocket.append(card1)
            
            if card1 <=N//2:
                pair[card1] = N-card1+1
            else:
                pair[N-card1+1] = card1
            plus -= 1
            coin -= 1
        
        #예외. pocket에 제출할 카드가 없는 경우
        if len(pair_pocket) == 0 and coin >=2:
            if card1 + card2 == N+1:
                pocket.append(card1)
                pocket.append(card2)
                pair_pocket.append([card1,N-card1+1])
                if card1<card2:
                    pair[card1] = card2
                else:
                    pair[card2] = card1
                coin -= 2
        
        return pocket,pair,pair_pocket,coin
        
        

def solution(coin, cards):

    pocket = []
    pair_pocket = []    #둘 다 pocket에 있는 카드쌍. 순서 상관 X. 카드 낼 때 사용
    global N, plus
    N = len(cards)
    cards_Q = deque(cards)
    pair = {}   #dictionary. 반드시 가져와야 하는 카드 쌍. 순서 상관 O
    round = 0
    
    #1. 처음 카드 뭉치에서 n/3개 뽑기
    plus = 0    #카드 뭉치에서 겹치는 경우 
    for _ in range(N//3):
        card = cards_Q.popleft()
        pocket.append(card)
        #이미 존재하는 경우
        if pair.get(card)!=None or pair.get(N-card+1)!=None:
            if coin-N//3 >= 0:
                plus += 1
            pair_pocket.append([card,N-card+1])
            continue
        
        if card <=N//2:
            pair[card] = N-card+1
        else:
            pair[N-card+1] = card
    
    #2. 
    while True:
        round += 1
        #종결조건1.카드 뭉치가 없는 경우
        if cards_Q == deque([]):
            break
        
        card1 = cards_Q.popleft()
        card2 = cards_Q.popleft()
        
        #카드 넣을지 말지 결정
        if coin>=1:
            pocket,pair,pair_pocket,coin = choose(card1,card2,pocket,pair,pair_pocket,coin)
        #print("pair_pocket",pair_pocket)
        
        #종결조건3.낼 수 있는 카드가 없는 경우
        if len(pair_pocket) == 0:
            break
        else:
            #3. pocket에서 N+1이 되는 카드쌍 제출
            del pair_pocket[0]
    
    return round

global N,plus

#3. 정확도 100. 직접 해결
#그리디 알고리즘

#이분탐색
def solution(coin, cards):

    N = len(cards)
    check = [0 for _ in range(N)]   #0은 앞의 수, 1은 앞의 N//3과 쌍이 되는 수, 2는 N//3과 쌍이 되지 않는 평범한 쌍의 뒤의 수 
    dict = {}   #먼저 나온 수가 key, 뒤에 나온 수가 value

    result = 0
    
    for k in range(N):
        #아직 지나지 않은 경우
        if dict.get(N-cards[k]+1) == None:
            dict[cards[k]] = N-cards[k]+1
        #쌍 중에서 뒤에 나오는 경우
        else:
            check[k] = 2
            
            #만약 앞의 N//3개인 경우 1로 저장
            for l in range(N//3):
                if N-cards[k]+1 == cards[l]:
                    check[k] = 1      
    
    use = [0,0]    #카드 사용하는데 필요한 coin 수. [15,16]인 경우 1 코인 사용해 15개 제출 가능,2 사용해 16쌍 존재
    
    for k in range(N//3):
        if check[k]==1:
            use[0] += 1
    coin += use[0]  #0~N//3인덱스까지는 코인을 쓰지 않고 낼 수 있으므로
    
    for k in range(N//3,N,2):
        #check[k]
        if check[k]==1:
            use[0] += 1
        elif check[k]==2:
            use[1] += 1

        #check[k+1]
        if check[k+1]==1:
            use[0] += 1
        elif check[k+1]==2:
            use[1] += 1
        
        #1 coin 낼 수 있는 카드쌍이 제출. 1 coin 낼 수 있으면 1 먼저 제출
        if use[0]>0 and coin>=1:
            use[0] -= 1
            coin -= 1
        else:
            #2 coin 제출
            if use[1]>0 and coin>=2:
                use[1] -= 1
                coin -= 2
            #2 coin도 낼 수 없는 경우 반환
            else:
                result = k
                break

        result = k
        
        #낼 카드가 더 있으면 한 라운드 후에 종료. result를 index로 설정했기에 2 증가해야 1 라운드 증가 
        if k==N-2 and use!=[0,0]:   
            result += 2
    #result는 종료 인덱스를 의미하며, N//3은 제외하고 몇 번 동작했는지 구해야함
    result = (result-N//3)//2 + 1
    return result