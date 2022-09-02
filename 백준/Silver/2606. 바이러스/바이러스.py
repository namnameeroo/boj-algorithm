n = int(input())
lines = int(input())
connection = [list() for _ in range(0, n + 1)]

# 연결
for i in range(lines):
    x, y = map(int, input().split())
    connection[x].append(y)
    connection[y].append(x)


# check = [0 for _ in range(0, n + 1)]
check = [0] * (n + 1)
cnt = 0


def virus(pc):
    global cnt
    check[pc] = 1

    for pc in connection[pc]:  # 1번 컴퓨터에서 시작해서 탐색,
        if check[pc] == 0:
            virus(pc)
            cnt += 1


virus(1)
print(cnt)
