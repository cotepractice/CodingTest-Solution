def solution(price, money, count):

    total = (price*(1+count)*count)//2
    if total<=money:
        return 0
    else :
        return (total-money)