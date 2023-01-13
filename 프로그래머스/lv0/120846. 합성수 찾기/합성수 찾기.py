def solution(n):
    answer = n
    
    if n < 4:
        return 0
    
    def check(num):
        for k in range(2, int(num**0.5)+1 ):
            if num % k == 0:
                return True
        return False
    
    for i in range(1, n+1):
        if check(i)==False:
            answer -= 1
    return answer