# [PCCP 기출문제] 1번

#t초동안 붕대를 감으면 1초당 x만큼 체력 회복. t초연속 성공하면 y만큼 추가 회복
#최대체력 health
#몬스터의 공격시간과 피해량 attacks

def solution(bandage, health, attacks):
    j = 0   #attacks 
    continuous = 0  #지속시간
    result = 0
    max = health
    
    for i in range(attacks[-1][0]+1):
        #attack 당하는 경우
        if (i == attacks[j][0]):
            health -= attacks[j][1]
            if (health<=0):
                result = -1
                break
            continuous = 0
            j += 1
            #print("i",i,"health1",health)
        #attack 안 당하는 경우
        else:
            continuous += 1
            if (continuous == bandage[0]):
                health += bandage[1] + bandage[2]
                continuous = 0
            else:
                health += bandage[1]
            if (health >= max):
                health = max
            #print("i",i,"health2",health)
    if (result == 0):
        result = health
            
    answer = result
    return answer
