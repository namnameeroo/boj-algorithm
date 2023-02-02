def calculate(str_sick):
    x, sym, y = str_sick.split(' ')
    if sym == '-':
        return int(x)-int(y)
    if sym == '+':
        return int(x)+int(y)

def solution(quiz):
    arr = []
    for each in quiz:
        sick, result = map(lambda x: x.strip(), each.split('='))
        print(sick, result)
        isCorrect = False
        if calculate(sick) == int(result):
            isCorrect = True
        arr.append('O' if isCorrect else 'X')
    return arr