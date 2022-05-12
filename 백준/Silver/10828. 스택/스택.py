import sys
input = sys.stdin.readline
n = int(input())
lst = []
for i in range(n):
    l =  list(input().split())
    if len(l)==2:   # push
        if l[0] == 'push':
            lst.append(l[1])
    else:
        order = l[0]
        if order == 'pop':
            if len(lst)==0:
                print(-1)
                continue
            print(lst.pop())

        elif order == 'size':
            print(len(lst))
        elif order == 'empty':
            print(1 if len(lst)==0 else 0)
        elif order == 'top':
            if len(lst)==0:
                print(-1)
                continue
            print(lst[-1])
