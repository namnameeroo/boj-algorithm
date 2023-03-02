def solution(n, m, section):
    # n 구역 수, 벽의 길이
    # m 롤러 한번에 칠해지는 길이
    # section 칠해야 할 구역
    
    paint_end = 0
    cnt = 0
    while paint_end <= n and section:
        sec = section.pop(0)
        if paint_end < sec:
            cnt += 1
            paint_end = sec+m-1
    
    return cnt