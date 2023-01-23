def solution(n):
    yacks = set()
    sosu = set()
    
    def updateYacksu(n):
        for i in range(1,int(n**0.5) +1):
            res, mok = n%i, n//i
            if res == 0:
                yacks.add(mok)
                yacks.add(i)
                
    def getYackCnt(n):
        local_yacks = set()
        for i in range(1,int(n**0.5) +1):
            res, mok = n%i, n//i
            if res == 0:
                local_yacks.add(mok)
                local_yacks.add(i)
        return len(local_yacks)
    
    def addSosu():
        # global sosu
        for num in yacks:
            if getYackCnt(num) == 2:
                sosu.add(num)
        
    updateYacksu(n)
    addSosu()
        
    return sorted(list(sosu))