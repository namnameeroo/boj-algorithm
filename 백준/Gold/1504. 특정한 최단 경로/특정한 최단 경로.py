# 다익스트라 알고리즘은 하나의 정점에서 나머지 모든 정점까지의 최단 거리를 찾는 알고리즘이다.
import sys
import heapq as hq
input = sys.stdin.readline

n, e = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    g[a].append([c, b])
    g[b].append([c, a])

v1, v2 = map(int, input().split())
# 1=> v1=> v2=>n
# 1=> v2=> v1=>n


def getDP(s):
    heap = []
    dp = [sys.maxsize] * (n + 1)
    dp[s] = 0
    hq.heappush(heap, [0, s])  # 초기값
    while heap:
        w, node = hq.heappop(heap)
        if dp[node] < w:
            continue
        for nextW, nextN in g[node]:
            nextW = nextW + w
            if nextW < dp[nextN]:
                dp[nextN] = nextW
                hq.heappush(heap, [nextW, nextN])
    # print(dp)
    return dp


def getDistance(s, e):
    dp = getDP(s)
    return dp[e]


v1v2 = getDistance(1, v1) + getDistance(v1, v2) + getDistance(v2, n)
v2v1 = getDistance(1, v2) + getDistance(v2, v1) + getDistance(v1, n)
result = min(v1v2, v2v1)
print(result if result < sys.maxsize else -1)
