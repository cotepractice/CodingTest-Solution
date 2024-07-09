
#1. 정확성 88.6/100.0
def solution(picks, minerals):
    answer = 0
    dict = {}
    if len(minerals)%5==0:
        minerals_lst = [[] for _ in range(len(minerals)//5)]
    else:
        minerals_lst = [[] for _ in range(len(minerals)//5 + 1)]
    
    idx = 0
    lst = [0,0,0]   #다이아, 철, 돌 곡괭이로 캘 때 드는 피로도
    for k in range(len(minerals)):
        if minerals[k] == "diamond":
            lst[0] += 1
            lst[1] += 5
            lst[2] += 25

        elif minerals[k] == "iron":
            lst[0] += 1
            lst[1] += 1
            lst[2] += 5

        else:
            lst[0] += 1
            lst[1] += 1
            lst[2] += 1
        
        #print(k,len(minerals)-1)
        if k!=0 and ((k+1)%5==0 or k==len(minerals)-1):
            #print("here")
            dict[idx] = lst
            minerals_lst[idx] = lst
            idx+=1
            lst = [0,0,0]
    
    minerals_lst.sort(reverse=True)
    #sorted_dict = sorted(dict.items(), key=lambda item:item[1], reverse=True)
    #print(minerals_lst)
    
    dia_N = picks[0]
    iron_N = picks[1]
    stone_N = picks[2]
    
    for k in range(len(minerals_lst)):
        #print(minerals_lst[k])
        a,b,c = minerals_lst[k][0],minerals_lst[k][1],minerals_lst[k][2]
        if dia_N != 0:
            answer += a
            dia_N -= 1
        else:
            if iron_N != 0:
                answer += b
                iron_N -= 1
            else:
                if stone_N != 0:
                    answer += c
                    stone_N -= 1
                else:
                    break
    
    return answer 

#2. 91.4/100.0. 가지고 있는 곡괭이로 캐려는 광석의 수가 주어진 광석보다 작은 경우, 뒤는 탐색할 수 없음 (주어진 순서대로만 캘 수 있기 때문) 

def solution(picks, minerals):
    answer = 0

    if len(minerals)%5==0:
        minerals_lst = [[] for _ in range(len(minerals)//5)]
    else:
        minerals_lst = [[] for _ in range(len(minerals)//5 + 1)]
    
    idx = 0
    lst = [0,0,0]   #다이아, 철, 돌 곡괭이로 캘 때 드는 피로도
    for k in range(len(minerals)):
        if minerals[k] == "diamond":
            lst[0] += 1
            lst[1] += 5
            lst[2] += 25

        elif minerals[k] == "iron":
            lst[0] += 1
            lst[1] += 1
            lst[2] += 5

        else:
            lst[0] += 1
            lst[1] += 1
            lst[2] += 1

        if k!=0 and ((k+1)%5==0 or k==len(minerals)-1):
            minerals_lst[idx] = lst
            idx+=1
            lst = [0,0,0]
    
    #곡괭이로 캘 수 있는 수보다 클 경우, 컷
    dia_N = picks[0]
    iron_N = picks[1]
    stone_N = picks[2]
    
    N = dia_N + iron_N + stone_N
    #print(minerals_lst)
    slice_lst = minerals_lst[:N]
    #print(minerals_lst)
    slice_lst.sort(reverse=True)
    
    dia_N = picks[0]
    iron_N = picks[1]
    stone_N = picks[2]
    
    for k in range(len(slice_lst)):
        if slice_lst == []:
            break
        a,b,c = slice_lst[k][0],slice_lst[k][1],slice_lst[k][2]
        if dia_N != 0:
            answer += a
            dia_N -= 1
        elif iron_N != 0:
            answer += b
            iron_N -= 1
        elif stone_N != 0:
            answer += c
            stone_N -= 1
        else:
            break
    
    return answer 

#3. 100/100. 이전에는 slice_lst[0]으로 정렬했는데, slice_lst[2]로 정렬하는 것이 더 정확
#반례: picks = [1, 1, 0], minerals = ["iron", "iron", "diamond", "iron", "stone", "diamond", "diamond", "diamond"]

def solution(picks, minerals):
    #picks = [1, 1, 0]
    #minerals = ["iron", "iron", "diamond", "iron", "stone", "diamond", "diamond", "diamond"]
    answer = 0

    if len(minerals)%5==0:
        minerals_lst = [[] for _ in range(len(minerals)//5)]
    else:
        minerals_lst = [[] for _ in range(len(minerals)//5 + 1)]
    
    idx = 0
    lst = [0,0,0]   #다이아, 철, 돌 곡괭이로 캘 때 드는 피로도
    for k in range(len(minerals)):
        if minerals[k] == "diamond":
            lst[0] += 1
            lst[1] += 5
            lst[2] += 25

        elif minerals[k] == "iron":
            lst[0] += 1
            lst[1] += 1
            lst[2] += 5

        else:
            lst[0] += 1
            lst[1] += 1
            lst[2] += 1

        if k!=0 and ((k+1)%5==0 or k==len(minerals)-1):
            minerals_lst[idx] = lst
            idx+=1
            lst = [0,0,0]
    
    #곡괭이로 캘 수 있는 수보다 클 경우, 컷
    dia_N = picks[0]
    iron_N = picks[1]
    stone_N = picks[2]
    
    N = dia_N + iron_N + stone_N
    #print(minerals_lst)
    slice_lst = minerals_lst[:N]
    print(slice_lst)
    slice_lst.sort(reverse=True,key=lambda x:x[2])
    
    dia_N = picks[0]
    iron_N = picks[1]
    stone_N = picks[2]
    
    for k in range(len(slice_lst)):
        if slice_lst == []:
            break
        a,b,c = slice_lst[k][0],slice_lst[k][1],slice_lst[k][2]
        if dia_N != 0:
            answer += a
            dia_N -= 1
        elif iron_N != 0:
            answer += b
            iron_N -= 1
        elif stone_N != 0:
            answer += c
            stone_N -= 1
        else:
            break
    
    return answer 