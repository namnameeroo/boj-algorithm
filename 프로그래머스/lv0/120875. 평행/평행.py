from itertools import combinations
def solution(dots):

    coms = list(combinations(dots, 2))
    for i in range(3):
        a,b = coms[i]
        c,d = coms[5-i]
        
        angle_1 = (a[1]-b[1])/(a[0]-b[0])
        angle_2 = (c[1]-d[1])/(c[0]-d[0])
        
        if angle_1 == angle_2:
            return 1
    
    return 0