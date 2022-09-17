"""
양 모으기, 
노드 방문 : 해당 노드의 양과 늑대가 따라온다.
늑대 : 모은 양의 수 <= 늑대 수 일 때, 모든 양 잡아먹음
조건 : 양 안 먹히게 하면서 최대한 많이 모아서 루트로 돌아오기

=> DFS?

"""


def solution(info, edges):
    answer = []
    visited = [0] * len(info)
    visited[0] = 1  # 루트는 양

    def DFS(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
        for i in range(len(edges)):  # 노드개수
            parent = edges[i][0]
            child = edges[i][1]
            isWolf = info[child]
            if visited[parent] and not visited[child]:
                visited[child] = 1
                DFS(sheep + (isWolf==0), wolf + isWolf)
                visited[child] = 0  # 여기 중요하다, 돌고 나오면 다시 복구하는 거인듯.

    DFS(1, 0)
    return max(answer)
