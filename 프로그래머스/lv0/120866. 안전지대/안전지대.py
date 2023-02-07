def solution(board):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    n = len(board)
    visited = [[False] * n for _ in range(n)]

    def check(x, y):
        if 0 <= x < n and 0 <= y < n:
            return True
        return False


    def bfs(bomb):
        x, y = bomb
        visited[x][y] = True
        cnt = 1
        for i in range(8):
            nx, ny = dx[i] + x, dy[i] + y
            if check(nx, ny) and visited[nx][ny] == False and board[nx][ny]==0:

                visited[nx][ny] = True
                cnt += 1

        return cnt


    result = 0
    for r in range(n):
        for c in range(n):
            cnt = 0
            if visited[r][c] == False and board[r][c] == 1:
                visited[r][c] = True
                cnt = bfs([r, c])

            result += cnt
    # print(n * n - result)
    return n * n - result
