import math

def check(number_bin, prev_parent):#number_bin은 이진수 리스트 슬라이싱한 리스트, prev_parent는 이전 부모가 "1"인지 여부 
    
    mid = len(number_bin)//2
    #number_bin이 비어 있지 않은 경우
    if number_bin:
        #bool 타입. 아래 자식이 "1"인 경우, son = True
        son = (number_bin[mid]=="1")
    #없으면 반환
    else:
        return 1
    
    #son이 있으면 그 위의 부모가 반드시 존재해야 함 
    if son and not prev_parent:
        return 0
    else:
        return check(number_bin[mid+1:],son) and check(number_bin[:mid],son)
    
    
def sol(number):
    if number == 1:
        return 1
    
    number_bin = bin(number)[2:]
    
    #이진트리는 2^n - 1 형태
    #math.log(x,2) = log_2(X)
    digit = 2 ** (int(math.log(len(number_bin), 2)) + 1) - 1
    number_bin = "0" * (digit - len(number_bin)) + number_bin

    if number_bin[len(number_bin)//2]=="1" and check(number_bin, True):
        return 1
    else:
        return 0
    
def solution(numbers):
    answer = []
    
    for number in numbers:
        answer.append(sol(number))
        
    return answer