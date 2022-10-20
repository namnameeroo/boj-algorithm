import sys
input = sys.stdin.readline
n, m = map(int, input().split())
g = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    g[a][b] = 1

for mid in range(n+1):
    for short in range(n+1):
        for tall in range(n+1):
            if g[short][mid]==1 and g[mid][tall]==1:
                g[short][tall] = 1

result = 0
for start in range(n+1):
    cnt = 0
    for end in range(n+1):
        cnt += g[start][end]+g[end][start]
        
    if cnt == n-1:
        result += 1
            
print(result)
