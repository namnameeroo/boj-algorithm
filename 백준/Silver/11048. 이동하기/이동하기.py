import sys
input = sys.stdin.readline

n, m = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (m + 1) for _ in range(n + 1)]
# row = n
# col = m


dx = [1, 0, 1]
dy = [0, 1, 1]


def checkRange(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    else:
        return False


for i in range(1, n + 1):
    for j in range(1, m + 1):
        ans = 0
        for k in range(3):
            ni, nj = i - dx[k], j - dy[k]
            ans = max(ans, dp[ni][nj])
        dp[i][j] = miro[i - 1][j - 1] + ans


print(dp[-1][-1])
