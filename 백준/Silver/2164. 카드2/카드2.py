from collections import deque

def solutions(que):
    while len(que) > 1:
        que.popleft()
        num = que.popleft()
        que.append(num)

    return que.popleft() if len(que) == 1 else False


n = int(input())
q = [i for i in range(1, n + 1)]
queue = deque(q)
result = solutions(queue)
print(result)
