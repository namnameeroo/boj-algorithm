# 집 n개
# 공유기 c개
# 한 집에 하나, 가장 멀리씩 설치 max d

import sys
input = sys.stdin.readline
n,c = map(int, input().split())
house = sorted([int(input()) for _ in range(n)])

def getCnt(mid):
    cnt = 1
    idx = house[0]

    for i in house[1:]:
        if i >= idx + mid:
            idx = i
            cnt +=1

    return cnt

low = 1
high = house[-1] - house[0]
while low<=high:
    mid = (low + high)//2
    # 공유기 거리
    if getCnt(mid) >= c:
        answer = mid
        low = mid+1
    else:
        high = mid-1

print(answer)
