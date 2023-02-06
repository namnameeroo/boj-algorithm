def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2


# def solution(spell, dic):
#     answer = 2
#     checked = [0]*len(spell)
#     check_dir = {key:idx for idx, key in enumerate(spell)}
    
#     for word in dic:
#         for letter in word:
#             if letter in check_dir.keys():
#                 idx = check_dir[letter]
#                 checked[idx] += 1        
        
#         if 0 not in checked:
#             return 1

#         checked = [0]*len(spell)

#     return answer