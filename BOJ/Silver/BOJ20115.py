# https://www.acmicpc.net/problem/20115

n = int(input())
drink_list = sorted(map(int, input().split()))

std = drink_list.pop()
for drink in drink_list:
  std += drink/2
print(std)