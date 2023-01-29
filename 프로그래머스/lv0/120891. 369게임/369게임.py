def solution(order):
    result = 0
    target = [3,6,9]
    order = str(order)
    for each in order:
        if int(each) in target:
            result += 1
    return result