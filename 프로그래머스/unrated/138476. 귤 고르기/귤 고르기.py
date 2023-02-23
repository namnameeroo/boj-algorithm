from collections import Counter
def solution(k, tangerine):
    cnt = 0
    for tan in sorted(Counter(tangerine).values(),reverse=True):
        cnt += 1
        k -= tan
        if k <= 0:
            break
    return cnt