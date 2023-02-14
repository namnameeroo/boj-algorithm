def solution(score):
    # avg_list = [평균, 자리번호]
    avg_list = [[(x[0]+x[1]), idx] for idx, x in enumerate(score)]
    
    # ranked[자리번호] = 랭크번호
    ranked = [-1]*len(score)

    rank = 0
    same_cnt = 0
    pre = -1
    
    for avg, id in sorted(avg_list, reverse=True):
        num = avg_list[id][0]
        if pre != num:
            rank = rank + 1 + same_cnt
            same_cnt = 0
            pre = num
        else:
            same_cnt += 1
        ranked[id] = rank
        
    return ranked