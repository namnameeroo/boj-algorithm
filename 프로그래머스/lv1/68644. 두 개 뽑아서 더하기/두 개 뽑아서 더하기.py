from itertools import combinations

def solution(n):
    comb = set(map(sum,(combinations(n, 2))))
    return sorted(list(comb))
