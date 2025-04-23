#백준 #14500 테트로미노
import sys

input = sys.stdin.readline
#1. Python3로 해결하는 경우 시간 초과 발생 -> PyPy3로 제출하는 경우 성공
#회전
def rotate(block):
    return [[y,-x] for x,y in block]
#대칭
def symmetry_x(block):
    return [[-x,y] for x,y in block]

def symmetry_y(block):
    return [[x,-y] for x,y in block]

#Main
N,M = map(int,input().split())
boards = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    boards[i] = list(map(int,input().split()))

# ㅡ, ㅁ, ㄴ, 5, ㅜ
base_blocks = [[[0,0],[0,1],[0,2],[0,3]],
          [[0,0],[0,1],[1,0],[1,1]],
          [[0,0],[1,0],[2,0],[2,1]],
          [[0,0],[1,0],[1,1],[2,1]],
          [[0,0],[0,1],[0,2],[1,1]]
          ]

#가능한 모든 block 경우의 수. 겹치면 안 됨
blocks = set()

for base in base_blocks:
    current = base
    #1.회전
    for _ in range(4):
        normalized = tuple(sorted((x,y) for x,y in current)) #+) tuple과 sorted 사용 시 괄호에 유의
        blocks.add(normalized) #+) set()에 데이터 넣을 때에는 append 아니고 add
        #2.대칭
        sym1 = symmetry_x(current)
        sym2 = symmetry_y(current)    
        normalized_sym1 = tuple(sorted((x,y) for x,y in sym1))
        normalized_sym2 = tuple(sorted((x,y) for x,y in sym2))
        blocks.add(normalized_sym1)
        blocks.add(normalized_sym2)
        current = rotate(current)

answer = -1*float("inf")
for x in range(N):
    for y in range(M):
        for block in blocks:
            ans=0
            valid = True
            for dx,dy in block:
                nx,ny = x+dx,y+dy
                if 0<=nx<N and 0<=ny<M:
                    ans += boards[nx][ny]
                else:
                    valid = False
                    break
            if valid==True:
                answer = max(answer,ans)

print(answer)
