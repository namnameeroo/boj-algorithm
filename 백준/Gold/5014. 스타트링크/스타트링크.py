from collections import deque
import sys

def BFS(f,s,g,u,d):
    q = deque()
    click = 0
    q.append((s, click))
    visited = [0] * (f+1)
    while q:
        s, click = q.popleft()
        if s == g:
            print(click)
            return
        if 1<= s <= f and visited[s] == 0:
            visited[s] = 1
            click += 1
            q.append((s+u, click))
            q.append((s-d, click))
    
    print('use the stairs')
    return

f,s,g,u,d = map(int, input().split())
BFS(f,s,g,u,d)
