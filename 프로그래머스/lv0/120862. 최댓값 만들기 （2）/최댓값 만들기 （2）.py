from itertools import combinations
def solution(numbers):
    max_result = -10**8
    for a,b in combinations(numbers,2):
        max_result = max(a*b, max_result)
    return max_result