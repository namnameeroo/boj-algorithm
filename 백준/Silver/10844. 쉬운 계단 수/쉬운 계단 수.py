import sys
input = sys.stdin.readline
n = int(input())
    
# 길이가 n인 계단 수
d = [[0]*10 for _ in range(n+1)]

for k in range(1,10):
    d[1][k] = 1

for i in range(2,n+1):
    for j in range(10):

        if j == 0:
            d[i][j] = d[i-1][1]
        elif j == 9:
            d[i][j] = d[i-1][8]
        else:
            d[i][j] = d[i-1][j-1] + d[i-1][j+1]
mod = 1000000000
print(sum(d[n]) % mod)
