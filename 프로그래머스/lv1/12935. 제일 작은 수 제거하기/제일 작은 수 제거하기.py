def solution(arr):
    arr.pop(arr.index(min(arr)))

    return [-1] if len(arr)==0 else arr