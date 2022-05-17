import sys
input = sys.stdin.readline

def war(yp,yh):
    mid = yh
    for l in g:
        a = l[1]
        h = l[2]
        if l[0] == 1: # 몬스터 만남
            mp = a
            mh = h
            round = (mh // yp)
            mh -= round * yp
            yh -= round * mp
            if mh<=0:
                yh += mp 
            if yh < 1:
                return False
        else: # 포션방
            yp += a
            yh = min(yh+h ,mid)
    return True


n, yp = map(int, input().split())
g = [ list(map(int, input().split())) for _ in range(n)]

low = 1
high = 10**17
# high = sum(max([gg[1]*gg[2]] for gg in g))

answer = 0
while low <= high:
    mid = (low+high)//2
    if war(yp, mid) == False:
        low = mid + 1

    else:
        high = mid - 1
        answer = mid

print(answer)
