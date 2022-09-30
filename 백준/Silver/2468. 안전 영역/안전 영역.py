import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
# g = [list(map(int, input().split())) for _ in  range(n)]
# print(g)
g = []
largest = 0
for _ in range(n):
    l = list(map(int, input().split()))
    largest = max(max(l),largest)
    g.append(l)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited = [[1]*n for _ in range(n)]
def DFS(vx, vy, d):
    global area
    # 물에 잠기면 나가
    if -1<vx<n and -1<vy<n and visited[vx][vy]==1 and g[vx][vy] > d:
        visited[vx][vy] = 0
        for i in range(4):
            DFS(vx+dx[i], vy+dy[i], d)
        return True
    return False
area = 0
d = 0
lst = [0]
while d <= largest+1:
    for i in range(n):
        for j in range(n):
            if visited[i][j]==1 and DFS(i, j, d) == True:
                area+=1
                # print('-- 출발', i,j,d)
    # print(area, d)
    lst.append(area)
    d+= 1
    area = 0
    visited = [[1] * n for _ in range(n)]
print(max(lst))

