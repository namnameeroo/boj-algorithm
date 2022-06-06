x = int(input())
cnt = 0

for n in range(1,int(x)+1):
    if n//10 <=9:
        cnt += 1
    lst = [int(nn) for nn in str(n)]

    if len(lst)>2:
        d = lst[0] - lst[1]
        flag = True
        for idx in range(len(lst)-1):
            if d != lst[idx] - lst[idx+1]:
                flag = False
                break
        if flag:
            cnt += 1

print(cnt)