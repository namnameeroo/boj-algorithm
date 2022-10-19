import sys
input = sys.stdin.readline

# 도시개수 node
n = int(input())

# 버스개수
m = int(input())
inf = sys.maxsize
g = [[inf] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = min(g[a][b], c)

for mid in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                g[i][j] = 0
            else:
                g[i][j] = min(g[i][mid] + g[mid][j], g[i][j])
for x in g[1:]:
    for gg in x[1:]:
        print(gg if gg < inf else 0, end=" ")
    print()