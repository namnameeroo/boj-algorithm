import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
island = [list(map(int, input().split())) for _ in range(N)]

SEA = 0
EARTH = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()
q.append((0, 0))

visited = [[False] * N for _ in range(N)]


def drawSector(start, sector):
    q = deque()
    q.append(start)
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        island[x][y] = sector
        for move in range(4):
            nx, ny = x + dx[move], y + dy[move]
            if 0 <= nx < N and 0 <= ny < N and island[nx][ny] == EARTH and not visited[nx][ny]:
                visited[nx][ny] = True
                island[nx][ny] = sector
                q.append((nx, ny))


def makeBridge(sec):
    global bridge
    dist = [[-1] * N for _ in range(N)]
    adventure = deque()

    for i in range(N):
        for j in range(N):
            if island[i][j] == sec:
                adventure.append([i, j])
                dist[i][j] = 0

    while adventure:
        x, y = adventure.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if island[nx][ny] != 0 and island[nx][ny] != sec:
                    # 내구역 아닌 땅 만나면
                    bridge = min(dist[x][y], bridge)
                    return

                if island[nx][ny] == SEA and dist[nx][ny] == -1:
                    # 바다 만나면

                    dist[nx][ny] = dist[x][y] + 1
                    adventure.append([nx, ny])


sector = 1
bridge = 10**5
for x in range(N):
    for y in range(N):
        if visited[x][y] == 0 and island[x][y] == EARTH:
            drawSector((x, y), sector)
            sector += 1
            break  # why 가능?


# 한번더 탐색하면서 다리 그려야 하나?
for sec in range(1, sector):
    makeBridge(sec)
print(bridge)

# print(q)
# for p in secChecked:
#     print(p)
# print(secChecked)
# print(q)


# 결과 : 메모리 초과
