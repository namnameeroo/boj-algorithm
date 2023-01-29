from collections import Counter
def solution(s):
    answer = ''.join(sorted([k for k, cnt in Counter(s).items() if cnt == 1]))
    return answer