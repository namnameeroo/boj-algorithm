

def checkThree(n):
    k = 0
    if n%3==0:
        return False
    for i in str(n):
        if i == '3':
            return False
        k += int(i)
    if k%3==0:
        return False
    return True

def solution(n):
    result = n
    jump_cnt = 0
    current_pointer = 1
    while current_pointer-jump_cnt != n+1:
        if not checkThree(current_pointer):
            # print(current_pointer)
            jump_cnt += 1
        current_pointer += 1
    # print(current_pointer)
        
    return current_pointer - 1