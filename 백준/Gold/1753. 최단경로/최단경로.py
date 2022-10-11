import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())
inf = sys.maxsize
dp = [inf] * (v + 1)

heap = []
graph = [[] for _ in range(v + 1)]


def Dijkstra(start):
    dp[start] = 0

    heapq.heappush(heap, (0, start))
    while heap:
        w, nowNode = heapq.heappop(heap)

        if dp[nowNode] < w:
            continue
        for nextW, nextNode in graph[nowNode]:
            nextW = nextW + w
            if nextW < dp[nextNode]:
                dp[nextNode] = nextW
                heapq.heappush(heap, (nextW, nextNode))


for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

Dijkstra(start)
for e in dp[1:]:
    print("INF" if e >= inf else e)
