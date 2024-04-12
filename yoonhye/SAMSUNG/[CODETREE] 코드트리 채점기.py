# url : 도메인/문제ID
# 0초에 채점 우선순위가 1이면서 url이 u0인 초기 문제에 대한 채점 요청이 들어옴
# 채점 대기 큐에 있는 task 중 정확히 u와 일치하는 url이 단 하나라도 존재하면 큐에 추가 X

import heapq
from collections import deque
from collections import defaultdict

#채점 요청 200
def request(t, p, url):
    domain, id = url.split('/')
    if url not in waiting_queue_url:
        heapq.heappush(waiting_queue, (p, t, domain, id))
        waiting_queue_url.add(url)

#채점 시도 300
def try_judging(T):
    if not judger:  #쉬고 있는 채점기가 없는 경우 요청 무시
        return

    #해당 task의 도메인이 현재 채점을 진행중인 도메인 중 하나라면 불가능
    #해당 task와 일치하는 도메인에 대해 가장 최근에 진행된 채점 시작 시간이 start, 종료 시간이 start+gap이었고,
    #현재 시간 t가 start+3*gap 보다 작으면 채점 불가

    can_not_judge = []
    success = False
    while(waiting_queue):
        p, t, domain, id = heapq.heappop(waiting_queue)
        if domain in judging_domain:
            can_not_judge.append((p,t,domain,id))
            continue
        if history.get(domain) != None:
            start, end = history[domain]
            gap = end-start
            if T < (start + 3*gap):
                can_not_judge.append((p, t, domain, id))
                continue
        success = True
        break

    if success: #채점 가능한 task가 단 하나라도 있다면
        n = heapq.heappop(judger)
        judging[n] = (T,domain,id)
        judging_domain.add(domain)
        url = domain+"/"+id
        waiting_queue_url.remove(url)

    for lst in can_not_judge:
        heapq.heappush(waiting_queue, lst)


#채점 종료 400
def finish(t, J_id):
    if judging.get(J_id) != None:
        start, domain, id = judging[J_id]
        history[domain] = (start, t)
        del judging[J_id]
        judging_domain.remove(domain)
        heapq.heappush(judger, J_id)

#채점 대기 큐 조회 500
def get_waiting_queue():
    print(len(waiting_queue))

Q = int(input())
num, N, u0 = map(str, input().split())
N = int(N)
judger = [int(i) for i in range(1,N+1)]
heapq.heapify(judger)

waiting_queue = []
heapq.heapify(waiting_queue)
waiting_queue_url = set()

judging = dict()
judging_domain = set()

history = dict()

#코드트리 채점기 준비
request(0, 1, u0)

for _ in range(Q - 1):
    req = list(map(str, input().split()))
    if req[0] == "200":
        t, p, url = int(req[1]), int(req[2]), req[3]
        request(t, p, url)
    elif req[0] == "300":
        t = int(req[1])
        try_judging(t)
    elif req[0] == "400":
        t, J_id = int(req[1]), int(req[2])
        finish(t, J_id)
    else:
        get_waiting_queue()

