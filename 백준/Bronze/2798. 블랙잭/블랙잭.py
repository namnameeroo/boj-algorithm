from itertools import combinations

N, M = map(int, input().split())
clst = list(map(int,input().split()))

mac = 0
for cards in combinations(clst, 3):
    if mac <= sum(cards) <= M:

        mac = sum(cards)
print(mac)