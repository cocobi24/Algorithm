# https://www.acmicpc.net/problem/5543

burger = []
beverage = []

for i in range(3) :
  burger.append(int(input()))

for i in range(2) :
  beverage.append(int(input()))

burger.sort()
beverage.sort()
answer = burger[0] + beverage[0] - 50

print(answer)