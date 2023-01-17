from collections import deque

n, m = map(int, input().split())
miro = [list(int(x) for x in str(input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
visited = [list(False for _ in range(m)) for _ in range(n)]


def check(x, y):
    if 0 <= x < n and 0 <= y < m:
        if visited[x][y] == False:
            visited[x][y] = True
            return True
    return False


def bfs(x, y):
    q = deque()
    cnt = 1
    q.append([x, y, cnt])
    result = 0

    while q:
        x, y, cnt = q.popleft()
        visited[x][y] = True

        if x == n - 1 and y == m - 1:
            result = cnt
            break

        if miro[x][y] == 1:
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if check(nx, ny):
                    q.append([nx, ny, cnt + 1])
    return result


print(bfs(0, 0))
