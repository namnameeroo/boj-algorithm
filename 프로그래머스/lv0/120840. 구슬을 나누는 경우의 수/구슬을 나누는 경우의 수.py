import math
def solution(balls, share):
    return math.comb(balls, share)

# def solution(balls, share): # 각각은 구슬 개수
#     # 5개 중에 2개의 고르기
#     result = 1
#     if balls==share:
#         return 1
    
#     share = min(share, balls-share)
#     for dx in range(share):
#         result *= balls-dx
#         result /= (dx+1)
        
#     return int(result)
