def solution(num_list):
    odd, even = 0, 0
    for x in num_list:
        if x%2 == 0:
            even += 1
        else:
            odd += 1
    return [even, odd]