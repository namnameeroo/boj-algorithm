def solution(board):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    n = len(board)
    visited = [[False] * n for _ in range(n)]

    def check(x, y):
        if 0 <= x < n and 0 <= y < n:
            return True
        return False

    def adjacent(bomb):
        x, y = bomb
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
            new_danger = 0
            if board[r][c] == 1:
                new_danger = adjacent([r, c])

            result += new_danger

    return n * n - result
