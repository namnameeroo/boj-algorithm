

def solution(s):
    
    return ''.join(sorted([ x for x in set(s) if s.count(x)==1]))

# 풀이 1
# from collections import Counter
# answer = ''.join(sorted([k for k, cnt in Counter(s).items() if cnt == 1]))
    

# 풀이 2
# def solution(s):
#     hist = set()
#     onlys = set()
#     for each in s:
#         if each not in hist:
#             onlys.add(each)
#             hist.add(each)
#         else:
#             onlys.discard(each)
#     return ''.join(sorted(onlys))