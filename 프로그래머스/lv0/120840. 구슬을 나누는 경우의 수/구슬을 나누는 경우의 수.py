
def solution(balls, share): # 각각은 구슬 개수
    # 5개 중에 2개의 고르기
    result = 1
    if balls==share:
        return 1
    
    share = min(share, balls-share)
    for n in range(balls-share,balls):
        result*=(n+1)
    for m in range(share):
        result /= (m+1)
    
    return int(result)
