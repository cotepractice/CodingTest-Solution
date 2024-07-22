def convert_time(time):
    h,m = map(int,time.split(":"))
    return h*60 + m
    
def solution(book_time):
    dic = {}
    for book in book_time:
        st = convert_time(book[0])
        en = convert_time(book[1])
        for t in range(st,en+10):
            if dic.get(t) == None:
                dic[t] = 1
            else:
                dic[t] += 1
    
    return max(dic.values())