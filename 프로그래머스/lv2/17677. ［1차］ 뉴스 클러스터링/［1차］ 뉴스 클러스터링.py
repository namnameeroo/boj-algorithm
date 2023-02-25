def solution(str1, str2):
    answer = 0
    def getJachard(a,b):
        tempB=list(b)
        common=[]
        for each in a:
            if each in tempB:
                tempB.remove(each)
                common.append(each)
        # print('common : ', common)
        return round(len(common)/(len(a)+len(tempB)),7)
    
    def getPairs(word):
        result = []
        for idx in range(0,len(word)):
            pair = word[idx:idx+2]
            if pair.isalpha() and len(pair)==2:
                result.append(pair.upper())
        return result
    
    str1_lst = getPairs(str1)
    str2_lst = getPairs(str2)
    if len(str1_lst)==0 and len(str2_lst)==0:
        return 65536
    result = getJachard(str1_lst, str2_lst)
    result *= 65536
    answer = int(result)
    return answer