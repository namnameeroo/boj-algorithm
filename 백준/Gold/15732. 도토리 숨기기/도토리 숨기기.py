import sys

n,k,d = map(int, input().split())
rules = [list(map(int, input().split())) for _ in range(k)]
# print(n,k,d)
# print(rules)
def dotori(mid):
    total = 0
    for s, e, step in rules:
        beta = min(e, mid)
        if s <= beta:
            cal = (beta-s) // step + 1
            total += cal

    return total

low, high = 1, 10**6
ans = 0
while low <= high:
    mid = (low+high)//2
    if dotori(mid) >= d:
        ans = mid
        high = mid -1
    else:
        low = mid + 1

print(ans)