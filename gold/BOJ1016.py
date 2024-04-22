# https://www.acmicpc.net/problem/1016

min_value, max_value = map(int,input().split())
count_list = [1] * (max_value - min_value + 1)

for i in range(2, int(max_value**0.5) + 1):
  temp = i**2
  while temp <= max_value:
    start = int(min_value / temp) * temp
    for j in range(start, max_value + 1, temp):
      if j < min_value:
        continue
      if count_list[j - min_value]:
        count_list[j - min_value] = 0
    temp **= 2
ans = sum(count_list)
print(ans)