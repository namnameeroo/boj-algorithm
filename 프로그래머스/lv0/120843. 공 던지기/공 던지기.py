def solution(numbers, k):

    
    # 1 2 => 11111...
    # 1 2 3 => 132132132
    # 1 2 3 4 => 1 3 1 3 1 3 
    
    long = len(numbers)
    return numbers[(2*(k-1))%long]