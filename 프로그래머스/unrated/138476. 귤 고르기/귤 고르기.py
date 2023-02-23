from collections import Counter
def solution(k, tangerine):
    # c_list = list([x,y] for x, y in Counter(tangerine).items())

    c_list = list(Counter(tangerine).items())
    c_list.sort(key = lambda x: (x[1],x[0]),reverse=True)
    cnt = 0

    for _, tan in c_list:
        cnt += 1
        k -= tan
        if k <= 0:
            break
        
    
    return cnt