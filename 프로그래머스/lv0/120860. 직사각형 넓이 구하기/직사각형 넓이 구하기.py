def solution(dots):

    dots.sort(key = lambda x : (x[0],x[1]))
    x1, y1 = dots[0]
    x2, y2 = dots[-1]
    answer = (x2-x1) * (y2-y1)    
    
    return answer