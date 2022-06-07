import heapq as hq
import sys
input = sys.stdin.readline

n = int(input())
lst = []
hq.heapify(lst)
for _ in range(n):
    x = input().rstrip()
    if not x.isdecimal() and x>0 and x%1 != 0:
        continue
    x = int(x)
    if x == 0:
        if lst:
            print(hq.heappop(lst)*(-1))
        else:
            print(0)
        continue
    hq.heappush(lst,-x)
    