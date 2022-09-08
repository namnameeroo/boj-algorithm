from collections import deque


def solution(queue1, queue2):

    answer = 0
    mid = sum(queue1) + sum(queue2)
    if mid % 2 != 0:
        return -1

    mid //= 2
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    while q1 and q2:
        if sum1 > mid:
            tmp = q1.popleft()
            sum1 -= tmp
            sum2 += tmp

        elif sum1 < mid:
            tmp = q2.popleft()
            q1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
        else:
            return answer
        answer += 1

    return -1
