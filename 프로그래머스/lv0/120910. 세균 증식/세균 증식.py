def solution(n, t):
    dp = [0] * (t+1)
    dp[0] = n
    for i in range(1,t+1):
        dp[i] = dp[i-1] *2

    return dp[t]