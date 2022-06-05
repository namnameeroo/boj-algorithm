import sys
sys.setrecursionlimit(10**4)
n = int(input())


def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def fiboDP(b):
    dp = [0]*(b+1)
    dp[1], dp[2] = 1,1
    dp_cnt =1

    for i in range(3,b):
        dp_cnt += 1
        if dp[i-1] == 0 :
            fiboDP(i-1)
        if dp[i-2] == 0 :
            fiboDP(i-2)
        dp[i] = dp[i-1]+dp[i-2]
#    print(dp_cnt)
    return dp_cnt

print(fibo(n),fiboDP(n))

