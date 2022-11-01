from collections import deque

def solution(board):
    N = len(board)
    empty = 0

    def check(x, y):
        if 0 <= x < N and 0 <= y < N:
            return True
        return False

    def moveToCol(lx, ly, rx, ry):
        result = []

        # 아래
        if 0 <= lx + 1 < N and board[lx + 1][ly] == empty and board[rx + 1][ry] == empty:
            result.append([lx + 1, ly, lx, ly])
            result.append([rx + 1, ry, rx, ry])  # 오른쪽 아래로 이동

        # 위
        if 0 <= lx - 1 < N and board[lx - 1][ly] == empty and board[rx - 1][ry] == empty:
            result.append([lx - 1, ly, lx, ly])  # 왼쪽 위로 이동
            result.append([rx - 1, ry, rx, ry])  # 오른쪽 위로 이동
        return result

    def moveToRow(tx, ty, bx, by):
        result = []
        # 왼쪽으로 이동
        if check(tx, ty - 1) and board[tx][ty - 1] == empty and board[bx][by - 1] == empty:
            result.append([tx, ty - 1, tx, ty])
            result.append([bx, by - 1, bx, by])
        if check(tx, ty + 1) and board[tx][ty + 1] == empty and board[bx][by + 1] == empty:
            result.append([bx, by, bx, by + 1])  # 오른쪽으로 이동
            result.append([tx, ty, tx, ty + 1])

        return result

    def bfs(ax, ay, bx, by):
        q = deque()
        q.append(([ax, ay, bx, by], 0))
        hist = [[ax, ay, bx, by]]

        while q:
            xys, cnt = q.popleft()
            x1, y1, x2, y2 = map(int, xys)
            if (x1 == N - 1 and y1 == N - 1) or (x2 == N - 1 and y2 == N - 1):
                return cnt
            candi = []
            # 평행이동
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx1, ny1 = x1 + dx, y1 + dy
                nx2, ny2 = x2 + dx, y2 + dy
                if (
                    check(nx1, ny1)
                    and check(nx2, ny2)
                    and board[nx1][ny1] == empty
                    and board[nx2][ny2] == empty
                ):
                    candi.append([nx1, ny1, nx2, ny2])

            # 회전
            if x1 == x2:  # 가로로 놓여있음
                candi += moveToCol(x1, y1, x2, y2)
            else:
                candi += moveToRow(x1, y1, x2, y2)
            for temp in candi:
                if temp not in hist:
                    q.append((temp, cnt + 1))
                    hist.append(temp)

    cnt = bfs(0, 0, 0, 1)
    return cnt
