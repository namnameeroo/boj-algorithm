# R T 
# C F 
# J M 
# A N
# [0,1,2,3]

def solution(survey, choices):
    answer = ''
    score = [0,3,2,1,0,1,2,3]
    pair = ["RT","FC","JM","AN"]
    dic = {x:0 for x in "RT"+"FC"+"JM"+"AN"}

    for idx in range(len(survey)):
        c = choices[idx]
        if (c!=4):
            type = survey[idx][c//4]
            dic[type] += score[c]
    for i in range(4):

        if (dic[pair[i][0]]>dic[pair[i][1]]):
            answer += pair[i][0]
        elif (dic[pair[i][0]]<dic[pair[i][1]]):
            answer += pair[i][1]
        else :
            
            answer += sorted(list(pair[i]))[0]
            
    return answer