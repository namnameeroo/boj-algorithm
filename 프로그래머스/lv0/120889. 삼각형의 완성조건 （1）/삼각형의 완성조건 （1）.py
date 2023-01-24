def solution(sides):
    big = max(sides)
    return 1 if big < sum(sides)-big else 2

# def solution(sides):
#     sides.sort()
#     return 1 if sides[-1] < sides[0]+sides[1] else 2