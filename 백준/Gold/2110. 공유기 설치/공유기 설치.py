import sys
input = sys.stdin.readline
n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))
houses.sort()

left = 1
right = max(houses) # 가장 먼 집을 기준으로
while left <= right:
    mid = (left+right)//2
    cnt = 1
    cur = houses[0]
    for i in range(1, len(houses)):
        if houses[i] >= cur + mid:
            cnt += 1
            cur = houses[i]

    if cnt >= c:
        left = mid + 1
    else:
        right = mid - 1

print(right)