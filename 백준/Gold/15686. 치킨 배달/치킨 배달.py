from itertools import combinations
import sys

input = sys.stdin.readline
# sys.stdin = open('input.txt','rt')

n,m = list(map(int,input().split()))
g = [list(map(int,input().split())) for _ in range(n)]

houses = []
chicks =[]
for i in range(n):
    for j in range(n):
        if g[i][j]==1:
            houses.append([i,j])
        if g[i][j]==2:
            chicks.append([i,j])
result = 10**5
for ch in combinations(chicks, m):
    temp = 0
    for h in houses:
        dis = 10**3
        for j in range(m):
            
            dis = min(dis, abs(h[0]-ch[j][0])+abs(h[1]-ch[j][1]))
        temp += dis
    result = min(result, temp)
print(result)