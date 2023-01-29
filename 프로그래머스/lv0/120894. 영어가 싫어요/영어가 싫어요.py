def solution(numbers):
    answer = ''
    dic = { "zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    
    word = ''
    for letter in numbers:
        word += letter
        if word in dic.keys():
            answer += str(dic[word])
            word = ''
    
    return int(answer)