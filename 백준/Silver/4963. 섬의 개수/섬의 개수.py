import sys
input = sys.stdin.readline

# g[h][w]
# w 열의 개수,
# h 행의 개수,
dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,1,-1,1,-1,-1,1]
def DFS(x,y):
    global comp
    if 0<=x<h and 0<=y<w and g[x][y]==1:
        g[x][y] = 0

        # for n in range(8):
        #     print(dx[n],dy[n])
        #     DFS(x+dx[n], y+dy[n])
        #     return True
        DFS(x+dx[0], y+dy[0])
        DFS(x+dx[1], y+dy[1])
        DFS(x+dx[2], y+dy[2])
        DFS(x+dx[3], y+dy[3])
        DFS(x+dx[4], y+dy[4])
        DFS(x+dx[5], y+dy[5])
        DFS(x+dx[6], y+dy[6])
        DFS(x+dx[7], y+dy[7])

        return True

    else:
        return False




while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break

    g = [list(map(int, input().split())) for _ in range(h)]

    comp = 0
    for x in range(h):
        for y in range(w):
            if DFS(x, y) == True:
                comp += 1
    print(comp)
