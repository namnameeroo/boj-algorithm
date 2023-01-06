import re
def solution(my_string, letter):
    answer = re.sub(letter,'', my_string)
    return answer