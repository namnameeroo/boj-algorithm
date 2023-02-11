def gcd(x,y):
    big,small = max(x,y), min(x,y)
    mok = big//small
    res = big%small
    if res != 0:
        return gcd(small, res)
    else:
        return small
    
def solution(a, b):
    answer = 1
    gcd_num = gcd(a,b)
    
    if gcd_num != 1:
        b = b//gcd_num
    print(gcd_num,b)
    
    ys = set()
    for i in range(2,int(b**0.5)):
        print(i)
        if b%i == 0:
            if i!=2 or b//i != 2 or i!=5 or b//i != 5:
                answer = 2
                break
            ys.add(i)
            ys.add(b//i)
    print(ys)
    return answer