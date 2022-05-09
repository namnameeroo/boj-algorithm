import sys

case = 0
while True:
    l,p,v = map(int, input().split())
    if l*p*v == 0:
        break

    if v % p > l:
        res = l
    else:
        res = v % p

    answer = (v // p) * l + res
    case += 1
    print(f'Case {case}: {answer}')
