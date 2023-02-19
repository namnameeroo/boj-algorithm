def solution(babbling):
    from itertools import permutations, combinations
    answer = 0
    a,ret = ['aya','ye','woo','ma'],[]
    for i in range(2,5):
        for t in list(combinations(a,i)):
            ret+=[''.join(s) for s in list(permutations(t))]
    for s in babbling:
        if s in ret+a: answer+=1
    return answer

# from itertools import permutations
# def solution(babb):
#     answer = 0
#     possible = ["aya", "ye", "woo", "ma"]
#     cand = []
#     for i in range(1,5):
#         for comb in permutations(possible, i):
#             cand.append(''.join(comb))
#             # if ''.join(comb) in babb:
#             #     answer +=1 
#     for x in cand:
#         if x in babb:
#             answer += 1
#     return answer

