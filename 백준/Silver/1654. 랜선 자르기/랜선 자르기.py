import sys
input = sys.stdin.readline
k, n = map(int, input().split())

# lan = [int(input()) for _ in range(k)]
long = -1
lan = []
for _ in range(k):
    i = int(input())
    long=max(long,i)
    lan.append(i)


# n개의 랜선 만들어야 함
# 이미 k개 있음
# 같은 길이로 만들자
# 최대 길이는?

def getCnt(mid):
    tot = 0
    cnt = 0
    for i in range(k):
        cnt = lan[i]//mid
        tot += cnt
    return tot

low = 1
high = long
ans = 0
while low <= high:
    mid = (low + high)//2
    if getCnt(mid) >= n:
        ans = mid
        low = mid +1
    else:
        high = mid-1
print(ans)