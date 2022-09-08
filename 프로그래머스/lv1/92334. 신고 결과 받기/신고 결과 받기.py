
def solution(users, report, k):

    report = set(report)
    report = [text.split() for text in report]

    reported_cnt = {key:0 for key in users}
    reported_who = {key:[] for key in users}

    # block
    for content in report:
        whom = content[1]
        reported_cnt[whom] += 1
        reported_who[whom].append(content[0])
    
    blocked = [i for i, cnt in reported_cnt.items() if cnt >= k]

    result = [0] * len(users)
    for whom in blocked:
        multi_who = reported_who[whom]
        for who in multi_who:
            result[users.index(who)] +=1

        
    return result
        
