def solution(num, total):
    last = (2*total + (num*(num-1))) // (2*num)
    return list(range(last-num+1,last+1))