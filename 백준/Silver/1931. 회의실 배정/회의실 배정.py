import sys
input = sys.stdin.readline
n = int(input().rstrip())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort(key= lambda x: (x[1], x[0]))

time = -1
cnt = 0
for m in meetings:
    if m[0] >= time:
        time = m[1]
        cnt += 1

print(cnt)