def solution(routes):
    answer = 0
    
    prev_end = -30000
    routes.sort(key=lambda x: x[1])
    
    for route in routes:
        current_start,current_end = route
        if current_start>prev_end:
            answer+=1
            prev_end = current_end
    
    return answer