"""
양 모으기, 
노드 방문 : 해당 노드의 양과 늑대가 따라온다.
늑대 : 모은 양의 수 <= 늑대 수 일 때, 모든 양 잡아먹음
조건 : 양 안 먹히게 하면서 최대한 많이 모아서 루트로 돌아오기

=> BFS

"""

def solution(info, edges):
    answer = []
    visited = [0]+[0]*len(edges)
    visited[0] = 1 # start here
    
    def DFS(sheeps, wolves):
        if sheeps <= wolves:
            return
        answer.append(sheeps)
        for i in range(len(edges)):
            parent = edges[i][0]
            child = edges[i][1]
            isWolf = info[child]
            if visited[parent]==1 and visited[child]==0:
                visited[child]=1
                DFS(sheeps+(isWolf==0), wolves+isWolf)
                visited[child]=0

    
    DFS(1,0)

    return max(answer)

