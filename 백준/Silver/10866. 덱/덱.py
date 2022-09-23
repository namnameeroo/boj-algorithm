from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()
for i in range(n):
    userSay = input().split()

    if userSay[0] == "push_front":
        q.appendleft(userSay[1])
    elif userSay[0] == "push_back":
        q.append(userSay[1])
    elif userSay[0] == "pop_front":
        print(-1 if len(q) == 0 else q.popleft())
    elif userSay[0] == "pop_back":
        print(-1 if len(q) == 0 else q.pop())
    elif userSay[0] == "size":
        print(len(q))
    elif userSay[0] == "empty":
        print(1 if len(q) == 0 else 0)
    elif userSay[0] == "front":
        print(-1 if len(q) == 0 else q[0])
    elif userSay[0] == "back":
        print(-1 if len(q) == 0 else q[-1])
