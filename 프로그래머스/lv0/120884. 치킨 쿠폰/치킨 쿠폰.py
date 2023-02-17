def solution(chicken):
    service = 0
    while chicken > 0:
        if chicken >= 10:
            chicken -= 10
            service += 1
            chicken += 1
        else:
            chicken = 0
    return service