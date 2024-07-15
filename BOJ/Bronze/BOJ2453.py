# https://www.acmicpc.net/problem/2453

n, k = map(int, input().split())
temperature = list(map(int, input().split()))

max_temperature = -99999999
for i in range(n-k+1):
  temper = sum(temperature[i:i+k])
  if temper > max_temperature:
    max_temperature = temper
print(max_temperature)