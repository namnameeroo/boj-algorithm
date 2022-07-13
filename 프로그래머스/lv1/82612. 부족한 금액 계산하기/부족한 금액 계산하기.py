def solution(price, money, count):

    tot = sum(i*price for i in range(1, count+1))
    

    return tot-money if tot>money else 0