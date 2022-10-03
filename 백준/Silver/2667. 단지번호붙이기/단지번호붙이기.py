import sys
# input = sys.stdin.readline 
# => 뒤에서 strip 처리 해줘야해서 안쓰는 게 빠름
sys.setrecursionlimit(10**5)

NotHome = 0
Home = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


N = int(input())
G = [list(int(x) for x in str(input())) for _ in range(N)]
Visited = [[0] * N for _ in range(N)]

hCnt = 0  # 가구 수
sep = 0   # 단지 수
result = []

def DFS(x, y):
    global hCnt
    hCnt += 1  # 집 검사한 채로 호출된거니까 가구 수 up
    Visited[x][y] = 1

    for go in range(4):
        nx = x + dx[go]
        ny = y + dy[go]
        if 0 <= nx < N and 0 <= ny < N:
            if Visited[nx][ny] == 0 and G[nx][ny] == Home: # 방문 X, 집이면 DFS
                DFS(nx, ny)

for i in range(N):
    for j in range(N):
        if G[i][j] == Home and Visited[i][j] == 0:
            DFS(i, j) # 집인 곳에서 시작
            result.append(hCnt) # 가구 수 추가
            hCnt = 0  # 가구 수 초기화
            sep += 1  # 단지 수 up
print(sep)
result.sort()
for l in result:
    print(l)
