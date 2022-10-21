import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

def getPower(x, y):
    return s[x][y] + s[y][x]

comb = list(combinations(range(n), n // 2))
gap = sys.maxsize
for i in range(len(comb) // 2):
    aPower = 0
    bPower = 0
    for a1, a2 in combinations(comb[i], 2):
        aPower += getPower(a1, a2)

    for b1, b2 in combinations(comb[-i - 1], 2):
        bPower += getPower(b1, b2)
        
    gap = min(abs(aPower - bPower), gap)
print(gap)
