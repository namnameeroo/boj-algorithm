from collections import deque

def solution(cSize, cities):
    answer = 0
    queue = deque()
    # 캐시 크기에 따른 실행시간 측정하기
    if cSize==0:
        return len(cities)*5
    
    memory = deque()
    time = 0
    for startIdx in range(0,len(cities),cSize):
        newInfo = cities[startIdx:startIdx+cSize]
        for i in range(len(newInfo)):
            info = newInfo[i].upper()
            if info in memory:
                time += 1
                memory.remove(info)

            else:
                time += 5
                if len(memory) >=cSize:
                    memory.popleft()
            memory.append(info)

    print(time)

    
    
    return time