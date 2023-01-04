def solution(slice, n):
    answer = 0
    for i in range(n):
        if n <= i*slice:
            return i
    return n//2+1