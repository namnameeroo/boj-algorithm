from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    dic = {'right':1, 'left':-1}
    numbers.rotate(dic[direction])
    
    return list(numbers)


# def solution(numbers, dir):
#     return [numbers[-1]]+numbers[:-1] if dir=='right' else numbers[1:]+[numbers[0]]