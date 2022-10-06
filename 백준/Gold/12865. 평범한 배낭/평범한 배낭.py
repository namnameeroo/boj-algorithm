import sys
input = sys.stdin.readline
n,k = map(int, input().split())
d = [[0]*(k+1) for _ in range(101)]
things = [[0,0]]
for num in range(n):
    w, v = map(int, input().split())
    things.append([w, v])

for i in range(1,n+1):
    for j in range(1, k+1):
        w = things[i][0]
        v = things[i][1]
        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)


print(d[n][k])
