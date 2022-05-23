import sys
from collections import Counter
n,m = map(int, input().split())
t = Counter(map(int, input().split()))

s = 1
e = 10**9

while s<=e:
    mid = (s+e)//2
    tot = sum((h-mid)*i for h,i in t.items() if h>mid)

    if tot >= m:
        s = mid+1
    elif tot <m:
        # ans = mid
        e = mid-1

print(e)