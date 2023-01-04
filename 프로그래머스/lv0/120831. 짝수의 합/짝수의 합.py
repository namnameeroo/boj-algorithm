def solution(n):
    answer = 0
    if n == 1:
        return 0
    for i in range(0, n+1, 2):
        answer += i
    return answer