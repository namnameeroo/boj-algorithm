import sys
n, m = map(int, input().split())
cost = [int(input()) for _ in range(n)]

# n 일 동안 쓸 돈 : 1
# m 번 인출 : 1
# k 원 인출 => 다만, 모자라면 다시 인출? ** 여기가 이해가 잘 안됐네

low = max(cost)
high = 10**9

def getCnt(mid):
    res = mid # 500
    cnt = 1
    for i in range(n):
        if (res - cost[i]) < 0 :
            res = mid
            cnt+=1
        res -= cost[i]
    return cnt

while low <= high:
    mid = (low+high) //2
    if getCnt(mid) > m:
        low = mid + 1
    else:
        ans = mid
        high = mid -1

print(ans)





