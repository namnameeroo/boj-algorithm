import sys
input = sys.stdin.readline
n = int(input())
lst = []

for i in range(n):
    res = 0
    l =  list(input().split())

    if len(l)==2:   # push

        if l[0] == 'push':
            lst.append(l[1])
    else:

        order = l[0]
        # print(order)
        if order == 'pop':
            if len(lst)==0:
                print(-1)
                continue
            res = lst.pop()
        elif order == 'size':
            print(len(lst))
            # continue
        elif order == 'empty':
            print(1 if len(lst)==0 else 0)
        elif order == 'top':
            if len(lst)==0:
                print(-1)
                continue
            res = lst[-1]

    if res !=0:
        print(int(res))