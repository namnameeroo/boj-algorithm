

def checkThree(n):
    if n % 3 == 0 or '3' in str(n):
        return False
    return True

def solution(n):
    result = n
    jump_cnt = 0
    current_pointer = 1
    while current_pointer-jump_cnt != n+1:
        if not checkThree(current_pointer):
            jump_cnt += 1
        current_pointer += 1
        
    return current_pointer - 1