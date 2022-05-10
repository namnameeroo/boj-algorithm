import sys
input = sys.stdin.readline

n, price = map(int, input().split())
coins = [int(input()) for _ in range(n)]

res = price
cnt = 0
while res != 0:
    c = coins.pop()
    if c <= res:
        cnt += res // c
        res = res % c

print(cnt)
