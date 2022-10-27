"""
1. 아이디어
- MST 기본문제
- 간선을 인접리스트에 넣기
- 힙에 시작점 넣고 시작
- 힙 빌 때까지, 다음의 작업을 반복
    - 힙의 최소값 꺼내서 해당 노드 방문 X:
        - 방문 표시, 비용 추가, 간선 힙에 추가
2. 시간 복잡도
- MST : O(ElogE)

3. 자료구조
- 간선 저장 인접리스트 : (무게, 노드)
- 힙 : (무게, 노드)
- 방문 : bool[]
- MST결과값 : int

"""

import sys
import heapq as hq

input = sys.stdin.readline
v, e = map(int, input().split())
edge = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)
rs = 0
for i in range(e):
    a, b, c = map(int, input().split())
    edge[a].append([c, b])
    edge[b].append([c, a])

heap = [[0, 1]]
while heap:
    w, eachNode = hq.heappop(heap)

    if visited[eachNode] == False:
        visited[eachNode] = True
        rs += w
        for nextW, nextN in edge[eachNode]:
            if visited[nextN] == False:
                hq.heappush(heap, [nextW, nextN])

print(rs)
