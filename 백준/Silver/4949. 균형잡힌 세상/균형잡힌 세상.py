while True:
    sen = str(input())
    stack = []
    # 종료 조건, 마지막줄
    if sen == '.':
        break

    # 하나씩 검사
    for i in sen:
        if i == '.': # 종료 조건
            break
        if i == "[" or i == "(":
            stack.append(i)
        if i == "]" :
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(-1)
                break
        if i == ")" :
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(-1)
                break
        
    if len(stack) == 0:
        print('yes')
    else:
        print('no')