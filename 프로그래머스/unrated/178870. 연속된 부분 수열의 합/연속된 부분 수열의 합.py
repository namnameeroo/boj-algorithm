
def solution(sequence, k):
    sp = 0
    ep = 1
    tot = sequence[0]
    sequence+=[0]
    answer = []
    chance = 1
    
    while not(sp >= ep or ep == len(sequence)):
        if tot < k :
            tot += sequence[ep]
            ep += 1
            
        elif tot > k:
            tot -= sequence[sp]
            sp += 1
            
        elif tot == k:
            # 길이, 시작인덱스, 마지막인덱스
            arr = [ep-sp, sp, ep-1]
            if (not answer) or answer[0] > arr[0]:
                answer = arr
            elif answer[0] == arr[0] :
                answer = arr if answer[1] > arr[1] else answer
            tot -= sequence[sp]
            sp += 1
    
    return answer[1:]