import sys
def threeSearch(l,r):
    while abs(r-l) > 1e-9:
        left3 = (2*l + r)/3
        right3 = (l + r*2)/3
        if dist(left3) > dist(right3):
            l = left3
        else:
            r = right3
    return dist(l)
    
def dist(t):
    mx = ax*t + bx*(1-t)
    my = ay*t + by*(1-t)
    kx = cx*t + dx*(1-t)
    ky = cy*t + dy*(1-t)
    return ((kx-mx)**2 + (ky-my)**2)**0.5
    # route = ((ax-bx)**2+(ay-by)**2)**(1/2)


ax, ay, bx, by, cx, cy, dx, dy = map(int, input().split())
print("%.16f" % threeSearch(0, 1))  # 비율은 1을 기준으로 
