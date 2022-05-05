import sys
from collections import deque
import sys

def BFS():
    global n
    global o
    q = deque()
    time = 0
    q.append((n,time))
    visited = [False]* (100001)

    while q:
        n, time = q.popleft()
        
        if n == o:
            print(time)
            break
        if 0<=n<100001 and visited[n]==False:
            visited[n] = True
            time += 1
            q.append((n+1,time))
            q.append((n-1,time))
            q.append((n*2,time))

            
n, o = map(int, input().split())
BFS()


