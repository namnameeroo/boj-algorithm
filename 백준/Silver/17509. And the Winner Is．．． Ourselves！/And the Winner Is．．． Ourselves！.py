import sys
input = sys.stdin.readline

sum = 0
time = []
for i in range(11):
    d,v = map(int, input().split())
    time.append([d,v])

time.sort()
pen = 0
for v,d in time:
    sum += v
    pen += sum+20*d
print(pen)