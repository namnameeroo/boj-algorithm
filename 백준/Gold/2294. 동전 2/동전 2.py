n, k = map(int, input().split())

coins = list(int(input()) for _ in range(n))
d = [10001] * (k+1)
d[0] = 0

for c in coins:
    for i in range(c, k+1):
        d[i] = min(d[i-c] + 1, d[i])

if d[k] == 10001:
    print(-1)
else:
    print(d[k])