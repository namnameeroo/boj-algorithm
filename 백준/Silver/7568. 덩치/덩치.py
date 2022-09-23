import sys

N = int(input())
user = []
for i in range(N):
    x, y = map(int, input().split())
    user.append((x, y))
# user.sort(key=lambda x: (x[0], x[1]))
for u in user:
    rank = 1
    for compet in user:
        if compet[0] > u[0] and compet[1] > u[1]:
            rank += 1
        elif compet[0] < u[0] and compet[1] < u[1]:
            continue
        else:
            # 랭크 같아야...
            continue
    print(rank, end=" ")

