import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
miro = [[0 for _ in range(m + 1)]]
miro += [[0] + [int(s) for s in str(input().rstrip())] for _ in range(n)]
visited = [[0] * (m + 1) for _ in range(n + 1)]
visited[1][1] = 1


# n행 m열
def check(x, y):
    if 1 <= x <= n and 1 <= y <= m and miro[x][y] == 1 and visited[x][y] == 0:
        return True
    else:
        return False


def bfs(x, y):
    q = deque()
    q.append((x, y))
    answer = 0
    move = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while q:
        x, y = q.popleft()
        if x == n and y == m:
            break
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if check(nx, ny):
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return visited


result = bfs(1, 1)
print(result[n][m])
