import heapq
import sys

input = sys.stdin.readline
n = int(input())

l = []
for i in range(n):
    s, t = map(int, input().split())
    l.append((s,t))
l.sort()

room = [0]
for s,t in l:
    if s >= room[0]:
        heapq.heappop(room)
    heapq.heappush(room, t)
print(len(room))