def solution(sides):
    sides.sort()
    long = sides[-1]
    short = sides[0]
    
    return 2*short -1