import re
def solution(my_string):
    pattern = re.compile('[0-9]')
    return sum(list(map(int, pattern.findall(my_string))))