COL, ROW = 0,1
INSTALL, DELETE = 1, 0

def check(stack, info):
    x,y,what = map(int, info)
    if what == COL:
        # 바닥 위에 있거나, 보의 한쪽 끝 위에 있거나, 다른 기둥 위
        #  [x+1,y]
        #         [x,y]
        # [x-1,y]
        case1 = [[x, y-1, COL]]
        case2 = [[x, y, ROW], [x-1, y, ROW]]
        
        if y == 0 :
            return True
        elif case1[0] in stack: 
            return True
        elif (case2[0] in stack) or (case2[1] in stack):
            return True
        
        
    elif what == ROW:
        # 한쪽이 기둥 위, 양쪽 끝이 보
        # [x,y]    [x+1,y]
        # [x,y-1]  [x-1, y-1]
        case1 = [[x, y-1, COL], [x+1, y-1, COL]]
        case2 = [[x-1, y, ROW], [x+1, y, ROW]]
        if (case1[0] in stack) or (case1[1] in stack):
            return True
        if (case2[0] in stack) and (case2[1] in stack):
            return True

    return False

def solution(size, frame):
    stack = [] # [[1,1,0],[1,0,0]] 설치 내용
    for order in frame:
        x,y,what,cmd = map(int, order)
        content = [x,y,what]
        if cmd == INSTALL:
            if check(stack, content):
                stack.append(content)
            
        elif cmd == DELETE:
            stack.remove(content)
            for res in stack:
                if not check(stack, res):
                    stack.append(content)
                    break

    stack.sort(key=lambda x : (x[0], x[1], x[2]))
    return stack



