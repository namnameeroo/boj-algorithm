def solution(s):
    lst = []
    for x in s.split():
        if x == 'Z':
            lst.pop()
        else:
            lst.append(int(x))
            
    return sum(lst)