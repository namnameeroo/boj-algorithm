import sys
from collections import deque
input = sys.stdin.readline


dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# BFS는 재귀가 필요없구나...
# 함수 안에 재귀 대신 q 반복문으로 푸는구나...
# BFS 호출은 한번만 하면 되는 것..!
def BFS(x,y,z, time):
    global l
    global r
    global c
    q = deque()
    q.append((x,y,z))
    time[x][y][z] = 1
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            ax = x+dx[i]
            ay = y+dy[i]
            az = z+dz[i]
            if 0<=ax<l and 0<=ay<r and 0<=az<c :
                if g[ax][ay][az] == 'E':
                    time[ax][ay][az] = time[x][y][z]
                    print("Escaped in {0} minute(s).".format(time[x][y][z]))
                    return
        
                if time[ax][ay][az]==0 and g[ax][ay][az] == '.':
                    time[ax][ay][az] = time[x][y][z] + 1
                    # print(time[ax][ay][az], ax,ay,az)
                    q.append((ax,ay,az))
               

    
    print('Trapped!')
# l 층수
# r 행
# c 열
while True:
    l,r,c = map(int, input().split())
    if l == 0 and r == 0 and c==0:
        break
    time = [[[0]*c for _ in range(r)] for _ in range(l)]

    # 한줄 표현
    # g = [[list(map(str, input())) for _ in range(r)] for __ in range(l)]
    g = []
    for il in range(l):
        gg = [list(map(str, input().strip())) for _ in range(r)]
        input() # blanc
        g.append(gg)

    for aa in range(l):
        for bb in range(r):
            for cc in range(c):
                # print(aa,bb,cc)
                if g[aa][bb][cc] == 'S':
                    x = aa
                    y = bb
                    z = cc
                if g[aa][bb][cc] == 'E':
                    ox = aa
                    oy = bb
                    oz = cc

    #S시작지점
    #E탈출지점

    BFS(x, y, z, time)
