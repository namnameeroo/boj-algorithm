def solution(a, b, n):
    bottles = n
    coke = 0
       
    while bottles >= a :
        service = (bottles//a)*b
        coke += service
        bottles = bottles%a + service

    return coke