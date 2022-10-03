import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

NotHome = 0
Home = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


N = int(input())
G = [list(int(x) for x in str(input().strip())) for _ in range(N)]
Visited = [[0] * N for _ in range(N)]

hCnt = 0
sep = 0
result = []

def DFS(x, y):
    global hCnt
    hCnt += 1
    Visited[x][y] = 1

    for go in range(4):
        nx = x + dx[go]
        ny = y + dy[go]
        if 0 <= nx < N and 0 <= ny < N:
            if Visited[nx][ny] == 0 and G[nx][ny] == Home:
                DFS(nx, ny)

for i in range(N):
    for j in range(N):
        if G[i][j] == Home and Visited[i][j] == 0:
            DFS(i, j)
            result.append(hCnt)
            hCnt = 0
            sep += 1
print(sep)
result.sort()
for l in result:
    print(l)
