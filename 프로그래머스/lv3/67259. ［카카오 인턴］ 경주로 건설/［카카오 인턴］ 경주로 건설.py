import sys
import collections

def solution(board):
    answer = 0
    INF = sys.maxsize
    n = len(board)
    answer = INF
    dd = [0,1,2,3]
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    dist = [[[INF for _ in range(len(board[0]))] for _ in range(len(board))] for _ in range(4)]
    # dist = [[[INF for _ in range(len(board[0]))] for _ in range(len(board))] for _ in range(4)]
    
    q = collections.deque()
    q.append([0,0,0,0])
    q.append([0,0,0,1])
    while q:
        y, x, cost, d = q.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<n and 0<=nx<n and board[ny][nx]==0:
                n_cost = cost+1
                if d != dd[i]:
                    n_cost += 5
                if dist[dd[i]][ny][nx]>n_cost:
                    dist[dd[i]][ny][nx]=n_cost
                    if ny==n-1 and nx==n-1:
                        continue
                    q.append([ny, nx, n_cost, dd[i]])
    for i in range(4):
        answer=min(answer, dist[i][n-1][n-1])
    answer*=100
    return answer
    
    

    