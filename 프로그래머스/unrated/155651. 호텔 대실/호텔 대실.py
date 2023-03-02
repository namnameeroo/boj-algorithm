def solution(book_time):
    answer = 0
    
    dp = [0]*3601
    def trans(time):
        h, m = map(int, time.split(':'))
        return h*60 + m
    
    min_book_time = [[trans(s), trans(e)] for s, e in book_time]
    min_book_time.sort()
    for start, end in min_book_time:
        dp[start] += 1
        dp[end+10] -= 1

    rooms = 0
    first = min_book_time[0][0]
    
    for timeAt in range(first,3601):
        dp[timeAt] += dp[timeAt-1]
        rooms = max(dp[timeAt], rooms)
    
    return rooms