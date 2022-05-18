n = int(input())
card = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

def binary(mid):
    return card[mid]

card.sort()
ans = []
for i in nums:
    l = 0
    r = n-1
    j = 0
    while l<=r:
        mid = (l+r)//2
        v = binary(mid)
        if v < i:
            l = mid+1
        elif v > i:
            r = mid-1
        else:
            j = 1
            break
    ans.append(j)
for a in ans:
    print(a, end=' ')