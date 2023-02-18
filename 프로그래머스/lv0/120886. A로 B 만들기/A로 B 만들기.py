def solution(before, after):
    dic = {}
    answer = 0
    for letter in before:
        if letter in dic.keys():
            dic[letter] += 1
        else:
            dic[letter] = 1

    for target in after:
        if (target in dic.keys()) and (dic[target] > 0):
            dic[target] -= 1
        else:
            return 0
    
    return 1
# from itertools import permutations
# def solution(before, after):
#     answer = 0
#     for attempt in permutations(before):
#         attempt = ''.join(attempt)
#         if attempt == after:
#             answer = 1
#             break
#     return answer