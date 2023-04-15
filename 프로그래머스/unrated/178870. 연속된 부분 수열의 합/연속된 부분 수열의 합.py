def solution(seq, goal):
    
    sp, ep = 0, 1
    part_sum = seq[0]
    ans_sp, ans_ep = 0, 10**7
    seq+=[0]
    
    # 합이 큰 경우 + 기타예외
        # sp += 1
    # 합이 작은 경우
        # ep += 1
    # 합이 같고 길이가 짧은 경우
        # 답에 할당
    
    while sp < ep < len(seq):
        if part_sum < goal:
            part_sum += seq[ep]
            ep+=1
        elif part_sum == goal and ans_ep-ans_sp > ep-sp:
            ans_sp, ans_ep = sp, ep
        else:
            part_sum -= seq[sp]
            sp+=1

    return ans_sp, ans_ep-1
    
            
            
        