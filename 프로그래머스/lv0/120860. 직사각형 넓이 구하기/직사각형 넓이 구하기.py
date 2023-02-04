def solution(dots):
    dots.sort()
    return (dots[0][0]-dots[-1][0])*(dots[0][1]-dots[-1][1])