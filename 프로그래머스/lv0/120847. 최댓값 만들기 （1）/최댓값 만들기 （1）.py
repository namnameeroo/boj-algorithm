import heapq as hq
def solution(numbers):
    answer = 0
    hq._heapify_max(numbers)
    x = hq.heappop(numbers)
    hq._heapify_max(numbers)
    y = hq.heappop(numbers)
    print(x,y)
    
    return x*y