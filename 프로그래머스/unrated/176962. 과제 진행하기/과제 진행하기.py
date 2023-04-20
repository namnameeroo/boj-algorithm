def solution(plans):
    # 1. 정해진 시간이 되면 과제를 시작한다.
    # 2. 진행중이던 건 멈춘다.
    # 3. 정해둔거 끝나면 멈춰둔거 한다
    # 4. 멈춰둔거 여러개면 마지막에 하던거 한다 => 스택
    
    # 과목 , 시작, 소요시간
    def getTime(time_str):
        h, m = map(int, time_str.split(':'))
        time_int = h*60+m
        return time_int
    
    wait = []
    done = []
    plans = sorted([[t, getTime(x), int(d)] for t,x,d in plans],key=lambda x: x[1]) + [["",24*60,100 ]]
    board = {title: res for title, _, res in plans}
    
    for idx, item in enumerate(plans[:-1]):
        title, start_at, duration = item
        next_start_at = plans[idx+1][1]
        '''
        1. done : 다음꺼까지 남은 시간 >= 소요시간
            1-1. wait 소모
            
        2. not done : 다음꺼까지 남은 시간 < 소요시간
            2-1. wait 으로 넘김
                 남은 시간 업데이트
         '''
        
        
        term = next_start_at - start_at
        
        if term < duration:    # CASE 2
            wait.append(title)
            board[title] = duration - term
        else:
            done.append(title)
            # finished
            finished_at = start_at + duration
            small_term = next_start_at - finished_at
            new_wait = wait[::]
            for w in wait[::-1]:
                if small_term <= 0:
                    break
                if finished_at + board[w] <= next_start_at:
                    done.append(w)
                    new_wait.pop()
                    small_term -= board[w]
                    finished_at += board[w]
                else:
                    board[w] -= small_term
                    break

            wait = new_wait
    
    return done+wait[::-1]