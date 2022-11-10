n = int(input())
result = -1
cnt = 0
while result != n:
    if cnt == 0:
        result = n
    cnt +=1
    strN = str(result)
    newN = sum([int(x) for x in strN])
    result = int(strN[-1]+str(newN)[-1])

        
print(cnt)
        