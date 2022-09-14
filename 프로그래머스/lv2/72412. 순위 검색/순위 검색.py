from itertools import combinations
# from bisect import bisectleft
a = ['cpp', 'java', 'python']
b = ['backend', 'frontend']
c = ['junior', 'senior']
d = ['chicken', 'pizza']

# 리스트 탐색 => binary
def getCnt(users, scoreCut):
    userLong = len(users)
    if userLong == 0:
        return 0
    if userLong == 1 :
        if int(users[0]) < scoreCut:
            return 0
        else:
            return 1

    s = 0
    e = userLong-1
    
    while s <= e:
        mid = (s+e)//2
        userScore = users[mid]
        if userScore < scoreCut:
            s = mid + 1
        if userScore >= scoreCut:
            e = mid - 1

    return userLong-s



def solution(info, query):
    utils = {name: id for id, name in enumerate([0]+a+b+c+d)}
    scoreTable = {}

    for user in info:
        row_user = user.split()
        # (a,b,c,d)
        # (_,b,c,d)
        # (a,_,c,d)
        # ...
        # (a,b,c,_)
        # (_,_,_,_)
        
        content, userScore = row_user[:4], int(row_user[-1])
        for long in range(5):
            keylist = list(combinations(content, long))
            # scoreTable = {''.join([str(utils[name]) for name in k]):[userScore] for k in keylist} # {코드 : 점수, 코드 : 점수}
            for i in keylist:
                keyCode = ''.join([str(utils[name]) for name in i])
                if scoreTable.get(keyCode):
                    scoreTable[keyCode].append(userScore)
                else:
                    scoreTable[keyCode] = [userScore]
                    

    for k in scoreTable.keys():
        scoreTable[k].sort()
    


    # query
    ans = []
    for q in query:
        row_query = q.replace('and','').split()
        # conditions, standScore = row_user[:-2], row_user[-1]
        conditions = [e for e in q.split() if e != 'and' and e !='-']
        qCode = ''.join([str(utils[name]) for name in conditions[:-1]])
        
        # qCode = ''.join(str(utils[name]) for name in )
        standScore = int(conditions[-1])
        cnt = 0
        if scoreTable.get(qCode):
            cnt = getCnt(scoreTable[qCode], standScore)
        ans.append(cnt)
    return ans
            

            
            
        
        

        
        
        
        

