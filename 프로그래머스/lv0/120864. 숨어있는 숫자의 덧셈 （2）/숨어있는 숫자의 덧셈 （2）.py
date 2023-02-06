
def solution(my_string):
    step1 = ''.join([x if x.isdecimal() else ' 'for x in my_string])
    return sum(map(int,step1.split()))
