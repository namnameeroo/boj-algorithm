def solution(a, b):
    tot =0
    for i in range(min(a,b),max(a,b)+1):
        tot += i
    return tot