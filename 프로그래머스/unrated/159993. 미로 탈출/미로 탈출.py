from collections import deque
def solution(maps):
    long_x = len(maps)
    long_y = len(maps[0])
    dy = [0, 1, -1, 0]
    dx = [1, 0, 0, -1]
    
    
    def checkRange(x,y):
        if 0<=x<long_x and 0<=y<long_y:
            return True
        return False
    
    def bfs(start, target):
        visited = [[False]*long_y for _ in range(long_x)]
        q = deque()
        flag=False
        for i in range(long_x):
            for j in range(long_y):
                if maps[i][j] == start:
                    q.append((i,j,0))
                    visited[i][j] = True
                    break
            if flag:
                break
        
        while q:
            x, y, duration = q.popleft()            
            if maps[x][y] == target:
                return duration

            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if checkRange(nx, ny) and maps[nx][ny] != 'X' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny,duration+1))
        return -1
    
    result1 = bfs('S', 'L')
    result2 = bfs('L', 'E')
    return result1+result2 if (result1!=-1 and result2!=-1) else -1