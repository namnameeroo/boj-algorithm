import sys
input = sys.stdin.readline
# sys.stdin = open("./in2.txt", "rt")
R, C = map(int, input().split())
board = [str(input()) for _ in range(R)]

hist = ""
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

max_cnt = 0
def move(x, y):
    global hist
    global max_cnt
    temp = hist
    hist += board[x][y]
    max_cnt = max(len(hist), max_cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0 <= ny < C:
            now = board[nx][ny]
            if hist.find(now) == -1:  # 없으면
                move(nx, ny)
    hist = temp  # 여기가 관건이네!!!!

move(0, 0)
print(max_cnt)
