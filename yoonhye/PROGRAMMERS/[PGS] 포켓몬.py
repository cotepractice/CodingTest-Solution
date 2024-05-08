#최대한 많은 종류의 포켓몬을 포함해서 N/2마리 선택
from collections import defaultdict
def solution(nums):
    N = len(nums)/2
    info = defaultdict(int)
    for n in nums:
        info[n] += 1
    if len(info) < N :
        return len(info)
    else:
        return N
