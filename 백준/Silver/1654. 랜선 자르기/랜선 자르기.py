import sys
input = sys.stdin.readline

l, m = map(int, input().split())
lst = []
lar = 0
for i in range(l):
    temp = int(input())
    lst.append(temp)
    lar = max(lar, temp)

MaxLen = lar
MinLen = 1


def Count(len):
    cnt = 0
    for p in lst:
        cnt += (p//len)
    return cnt

while (MinLen <= MaxLen) :
    mid = (MaxLen + MinLen) //2
    if Count(mid) >= m:
        MinLen = mid+1
        res = mid
    else :
        MaxLen = mid-1

print(res)