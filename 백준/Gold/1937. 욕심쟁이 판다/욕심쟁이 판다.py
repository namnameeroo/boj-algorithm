import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
forest = [list(map(int, input().split())) for _ in range(n)]
move = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def dfs(x, y):
    if dp[x][y] == -1:
        dp[x][y] = 0
        for dx, dy in move:
            nx, ny = x + dx, y + dy

            if n > nx >= 0 and n > ny >= 0 and forest[nx][ny] > forest[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny))
    return dp[x][y] + 1

# 되게되게 BFS같네 => DFS 섞어서 푸는구나...
# 이동할 수 있는 최대 칸 수 구하라, 단 값이 클때만 이동한다
# dp[좌표x][좌표y] = 횟수

dp = [[-1] * n for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans, dfs(i, j))
print(ans)