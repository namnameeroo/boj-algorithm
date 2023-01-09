def solution(lines):
    answer = 0
    hist = {}
    for s,e in lines:
        for idx in range(s,e):
            if idx not in hist.keys():
                hist[idx] = 1
            else:
                hist[idx] += 1
                if hist[idx]==2:
                    answer += 1
    return answer