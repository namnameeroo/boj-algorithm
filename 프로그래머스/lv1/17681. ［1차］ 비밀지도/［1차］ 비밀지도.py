def solution(n, arr1, arr2):
    answer = []
    # 크기 N
    for i in range(n):
        line = ''
        bin1 = str(bin(arr1[i]))[2:].zfill(n)
        bin2 = str(bin(arr2[i]))[2:].zfill(n)
        for j in range(n):
            if int(bin1[j])+int(bin2[j])==0:
                line += ' '
            else:
                line += '#'
        answer.append(line)
    
    return answer