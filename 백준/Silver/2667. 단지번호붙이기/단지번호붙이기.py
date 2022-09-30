import sys
input = sys.stdin.readline

size = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(size)]

apt = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def DFS(x,y):
    global cnt
    if 0<=x<size and 0<=y<size:

        if graph[x][y] == 1:
            cnt+=1
            graph[x][y] = 0

            for i in range(4):
                nx = dx[i]+x
                ny = dy[i]+y
                DFS(nx,ny)
            return True
        return False
    else:
        return False

cnt = 0

for i in range(size):
    for j in range(size):
        if DFS(i,j) == True:
            apt.append(cnt)
            cnt = 0
print(len(apt))
apt.sort()
for a in apt:
    print(a)
# print(apt)