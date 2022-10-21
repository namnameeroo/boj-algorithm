from itertools import permutations
import sys

input=sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def cal(a, b):
    return abs(a - b)

result = 0
for a in permutations(arr, n):
    tot = 0
    for i in range(n - 1):
        tot += cal(a[i], a[i + 1])
    result = max(tot, result)
print(result)
