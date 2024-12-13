from collections import defaultdict

import sys
sys.stdin = open("input.txt", "r")

for k in range(1,11):
    N = int(input())
    words = input() #str형
    ans = 1

    words_dict = defaultdict() #words_dict[0]={"("의 개수}, 순서대로 (),[],{},<> 
    words_dict[0] = 0
    words_dict[1] = 0
    words_dict[2] = 0
    words_dict[3] = 0
    for i in range(N):
        #print("i",i)
        if words[i] == "(":
            words_dict[0] += 1
        if words[i] == "[":
            words_dict[1] += 1
        if words[i] == "{":
            words_dict[2] += 1
        if words[i] == "<":
            words_dict[3] += 1

        if words[i] == ")":
            words_dict[0] -= 1
            if words_dict[0] < 0:
                ans = 0
                #print(words_dict)
                break
        if words[i] == "]":
            words_dict[1] -= 1
            if words_dict[1] < 0:
                ans = 0
                #print(words_dict)
                break
        if words[i] == "}":
            words_dict[2] -= 1
            if words_dict[2] < 0:
                ans = 0
                #print(words_dict)
                break
        if words[i] == ">":
            words_dict[3] -= 1
            if words_dict[3] < 0:
                ans = 0
                #print(words_dict)
                break
        
    for i in range(4):
        if words_dict[i] != 0:
            ans = 0
            #print(words_dict)
            break
    
    print("#",k, " ",ans, sep="")
    