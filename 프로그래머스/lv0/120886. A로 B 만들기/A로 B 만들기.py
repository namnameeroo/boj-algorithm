def solution(before, after):
    before=sorted(before)
    after=sorted(after)
    if before==after:
        return 1
    else:
        return 0

# from collections import Counter
# def solution(before, after):
#     return 1 if Counter(before)==Counter(after) else 0
