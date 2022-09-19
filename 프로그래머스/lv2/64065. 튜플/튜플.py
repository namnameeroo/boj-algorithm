# 중복 가능
# 순서 있음
# 유한
from itertools import combinations

def solution(s):
    s = s.split('},')
    # s = list(tuple(x.replace('{','').replace('}','').split(',')) for x in s)
    s =[x.replace('{','').replace('}','') for x in s]
    s.sort(key=lambda x: len(x))
    answer = []
    for i in s:
        temp = i.split(',')
        for j in temp:
            j = int(j)
            if j not in answer:
                answer.append(j)

    return answer