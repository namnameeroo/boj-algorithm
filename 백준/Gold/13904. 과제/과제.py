import sys
import heapq

n = int(input())
graph = []
limit = 0

for _ in range(n):
    d,w = map(int, input().split())
    graph.append([-w,d,w])

# graph.sort(key=lambda x : (x[0], x[1]), reverse=True)
heapq.heapify(graph)

done = [0]*1001
score = 0
while graph:
    order,d,w = heapq.heappop(graph)
    for i in range(d,0,-1):
        if done[i] == 0 :
            done[i] = w
            break
print(sum(done))