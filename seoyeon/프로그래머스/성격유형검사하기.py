#2022 KAKAO TECH INTERNSHIP

#survey[i]의 첫 번째 캐릭터는 i+1번 질문의 "비동의" 선택지 선택시 받는 성격
#survey[i]의 두 번째 캐릭터는 i+1번 질문의 "동의" 선택지 선택시 받는 성격
#choices는 1부터7까지 매우비동의(1),비동의(2),약간비동의(3),모르겠음(4),약간동의(5),동의(6),매우동의(7)
#비동의만을 기준으로 카운팅

def solution(survey, choices):
    char_list = ["R","T","C","F","J","M","A","N"]
    cnt = [0 for _ in range(8)]
    idx = 0
    ans = []
    
    for choice in choices:
        if (choice<4):  
            cnt[char_list.index(survey[idx][0])] += 1
        else:
            cnt[char_list.index(survey[idx][1])] += 1
        idx += 1
        
    for i in range(8):
        #앞의 수는(index 0,2,..) 뒤의 숫자와 비교해 char_list 찾기
        if (i%2==0):
            if (cnt[i] >= cnt[i+1]):
                ans.append(char_list[i])
            else:
                ans.append(char_list[i+1])

    answer = "".join(ans)
    return answer