from itertools import combinations
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

def getDistance(house, chick):
    return abs(house[0] - chick[0]) + abs(house[1] - chick[1])

C = 2
H = 1

chicks = []
houses = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == C:
            chicks.append((i, j))
        if line[j] == H:
            houses.append((i, j))


dis = sys.maxsize
for clist in combinations(chicks, m):
    tot = 0
    for h in houses:
        near = 2 * n
        for c in clist:
            near = min(getDistance(h, c), near)
        tot += near
    dis = min(dis, tot)
print(dis)
