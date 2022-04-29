import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n) ]
queue = deque([])

# 익은 애들 x,y 좌표 구해서 queue에 넣기
for i in range(n):
    for j in range(m):
        if g[i][j] == 1:
            queue.append([i,j])
# 2<= m 행의 수, 높이, y < 1001
# 2<= n 열의 수, 너비, x < 1001

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def BFS():
    # 익은 애들 꺼내
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]

            if 0<=a<n and 0<=b<m and g[a][b] == 0:
                queue.append([a,b])
                g[a][b] = g[x][y] + 1

BFS()
res = 0
for i in g:
    for j in i:
        if j == 0:
            print(-1)
            sys.exit(0)
        res = max(res, max(i))
print(res-1)