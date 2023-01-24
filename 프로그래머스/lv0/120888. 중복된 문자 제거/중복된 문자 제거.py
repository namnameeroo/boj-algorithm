def solution(my_string):
    answer = set()
    result = ''
    for letter in my_string:
        if letter not in answer:
            answer.add(letter)
            result += letter
        else:
            continue
    return result