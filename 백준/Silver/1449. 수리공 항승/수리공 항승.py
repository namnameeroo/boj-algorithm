import sys

n,l = map(int,input().split())
pipe = list(map(int, input().split()))
pipe.sort()
tape = 1
ts, te = pipe[0]-0.5, pipe[0]+0.5
for i in range(len(pipe)):
    if i == 0 :
        continue
    if pipe[i]+0.5 - ts <= l:
            te = pipe[i]+0.5
    else:
        ts = pipe[i]-0.5
        tape += 1
print(tape)