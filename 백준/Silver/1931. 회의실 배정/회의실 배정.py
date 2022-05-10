import sys
input = sys.stdin.readline
n = int(input().rstrip())
meeting = [list(map(int, input().split())) for _ in range(n)]
meeting.sort(key=lambda x: (x[1],x[0]))

ss, ee = meeting[0][0], meeting[0][1]
cnt = 1

for i in meeting[1:]:
    s,e = i[0], i[1]
    if ee <= s: # 다음회의보다 일찍 끝
        cnt += 1
        ee = e

print(cnt)