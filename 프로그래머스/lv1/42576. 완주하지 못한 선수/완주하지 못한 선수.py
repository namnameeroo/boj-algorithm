def solution(p, c):
    answer = ''
    dic = {}
    for i in p:
        if i in dic.keys():
            dic[i]+=1
        else:
            dic[i] = 1

    for cc in c:
        dic[cc] -=1
    for d in dic:
        if dic[d] == 1:
            answer = d
    return answer