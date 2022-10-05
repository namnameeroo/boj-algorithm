import sys

input = sys.stdin.readline

A = str(input().strip())
B = str(input().strip())
dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
# dp[A][B] = maxNum


for aidx in range(1, len(A) + 1):
    for bidx in range(1, len(B) + 1):
        if A[aidx - 1] == B[bidx - 1]:
            dp[aidx][bidx] = dp[aidx - 1][bidx - 1] + 1
        else:
            dp[aidx][bidx] = max(dp[aidx - 1][bidx], dp[aidx][bidx - 1])

print(dp[len(A)][len(B)])
