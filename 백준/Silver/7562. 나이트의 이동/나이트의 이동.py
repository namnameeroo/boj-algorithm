import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

dx = [-2, -1, 1, 2, -2, -1, 1, 2]
dy = [ 1, 2, 2, 1,  -1, -2, -2, -1]

# BFS는 재귀가 필요없구나...
# 함수 안에 재귀 대신 q 반복문으로 푸는구나...
# BFS 호출은 한번만 하면 되는 것..!
def BFS(x,y, ox, oy):
    global l
    global move
    q = deque()
    q.append([x,y])
    while q:
        a,b = q.popleft()
        if a==ox and b==oy:
            return
        for k in range(8):
            nx = a+dx[k]
            ny = b+dy[k]
            if 0<=nx<l and 0<=ny<l and check[nx][ny] == False:
                check[nx][ny] = True
                q.append([nx, ny])
                g[nx][ny] = g[a][b] + 1

for i in range(t):
    l = int(input())
    g = [[0]*(l) for _ in range(l)]
    check = [[False]*(l) for _ in range(l)]
    x, y = map(int, input().split())
    mx, my = map(int, input().split())
    BFS(x, y, mx, my)
    print(g[mx][my])
