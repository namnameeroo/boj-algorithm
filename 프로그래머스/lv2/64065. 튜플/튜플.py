# 중복 가능
# 순서 있음
# 유한
from collections import Counter

def solution(s):
    s = s.split(',')
    filtered = [''.join(list(filter(str.isdigit, word))) for word in s ]
    count =[int(name) for name,v in sorted(Counter(filtered).items(), key=lambda x: x[1], reverse=True)]

    return count