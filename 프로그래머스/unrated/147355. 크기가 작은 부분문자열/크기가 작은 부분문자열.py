def solution(t, p):
    answer = 0
    long_t = len(t)
    long_p = len(p)

    for i in range(0,long_t-long_p+1):
        if int(t[i:i+long_p]) <= int(p):
            answer+=1
    return answer