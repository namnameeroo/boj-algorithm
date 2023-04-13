
def solution(sequence, k):
    sp = 0
    ep = 1
    tot = sequence[0]
    
    sequence += [0]
    answer = [10**7]
    while sp < ep < len(sequence):
        if tot < k :
            tot += sequence[ep]
            ep += 1
            
        elif tot == k and answer[0] > ep-sp :
            answer = [ep-sp, sp, ep-1]
            
        else:
            tot -= sequence[sp]
            sp += 1
            
    
    return answer[1:]