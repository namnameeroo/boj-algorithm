x = int(input())
cnt = 0
if x < 100:
    print(x)
else:
    cnt = 99
    for s in range(111, x+1):
        if int(str(s)[2]) - int(str(s)[1]) == int(str(s)[1]) - int(str(s)[0]):
            cnt += 1
    print(cnt)