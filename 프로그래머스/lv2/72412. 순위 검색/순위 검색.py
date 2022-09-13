from itertools import combinations


    

def solution(info, query):
    answer = []
    dic = {}
    for person in info:
        content_key = person.split()
        score = int(content_key[-1])
        for i in range(5):
            comb =list(combinations(content_key[:4], i))
            for c in comb:
                c = ''.join(c)
                if dic.get(c):
                    dic[c].append(score)
                else:
                    dic[c] = [score]

    # dic = {k:sorted(v) for k, v in dic.items()}
    for k in dic.values():
        k.sort()
        
    for q in query:
        q = [x for x in q.split() if (x!='and' and x!='-')]
        
        q_key = ''.join(q[:-1])
        q_score = int(q[-1])
        cnt = 0
        
        if dic.get(q_key):
            v_sorted = dic[q_key]
            if len(dic[q_key]) == 1 :
                cnt = 1 if dic[q_key][0] >= q_score else 0
            elif v_sorted[-1] < q_score:
                cnt = 0
            else:
                s = 0
                e = len(v_sorted)-1
                
                while s<=e:
                    mid = (s+e)//2
                    if v_sorted[mid] >= q_score:  # go to smaller
                        e = mid-1
                    if v_sorted[mid] < q_score:  # go to bigger
                        s = mid+1
                cnt = len(v_sorted)-s
                
        answer.append(cnt)
        
    return answer
