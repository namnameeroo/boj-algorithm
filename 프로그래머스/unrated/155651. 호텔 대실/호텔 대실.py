def solution(book_time):
    def trans(time):
        h, m = map(int, time.split(':'))
        return h*60 + m
    
    dp = [0]*3601    
    min_start = 3601
    max_end = -1
    
    for start, end in book_time:
        start = trans(start)
        end = trans(end)
        min_start = min(min_start, start)
        max_end = max(max_end, end)
        
        dp[start] += 1
        dp[end+10] -= 1

    rooms = 0
    for timeAt in range(min_start,max_end):
        dp[timeAt] += dp[timeAt-1]
        rooms = max(dp[timeAt], rooms)
    
    return rooms