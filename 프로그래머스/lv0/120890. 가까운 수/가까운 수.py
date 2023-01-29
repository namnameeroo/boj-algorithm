def solution(array, n):
    answer = 0
    smallers = -1
    biggers = 10**3
    
    for num in array:
        if num <= n:
            smallers = max(smallers, num)
        else:
            biggers = min(biggers, num)
    # print(smallers, biggers)
    return smallers if n - smallers <= biggers - n else biggers