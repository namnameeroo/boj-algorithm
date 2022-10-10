import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
cards = list(map(int, input().split()))

nums.sort()

def binary(target):
    s = 0
    e = n-1
    result = 0
    while s <= e:
        mid = (s + e) // 2
        if target < nums[mid]:
            e = mid - 1
        elif target > nums[mid]:
            s = mid + 1
        elif target == nums[mid]:
            result = 1
            break
    return result


for t in cards:
    print(binary(t), end=" ")
