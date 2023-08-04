# https://www.acmicpc.net/problem/15720

b, c, d = map(int, input().split())
bugger = sorted(map(int, input().split()))
side = sorted(map(int, input().split()))
drink  = sorted(map(int, input().split()))
l = min(len(bugger), len(side), len(drink))

origin = sum(bugger) + sum(side) + sum(drink)
print(origin)

for i in range(l) :
    bugger[-1-i] = bugger[-1-i] * 0.9
    side[-1-i] = side[-1-i] * 0.9
    drink[-1-i] = drink[-1-i] * 0.9

sale = int(sum(bugger) + sum(side) + sum(drink))
print(sale)