# import  sys
# sys.stdin = open('./input.txt', 'rt')

n = int(input())
arr = list(map(int, input().split()))
from itertools import permutations

temp = []
for p_arr in permutations(arr, len(arr)):
    tot = 0
    for i in range(1,len(arr)):
        tot+=abs(p_arr[i-1]-p_arr[i])
    temp.append(tot)
print(max(temp))
