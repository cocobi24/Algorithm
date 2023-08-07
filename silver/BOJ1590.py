# https://www.acmicpc.net/problem/1002

N, T = map(int, input().split())
bus_list = []

for _ in range(N) :
  S, I, C = map(int, input().split())
  bus_list.append(S)
  for i in range(1, C) :
    bus_list.append(S + I * i)

bus_list = sorted(filter(lambda x: x >= T, bus_list))
if len(bus_list) > 0 :
  print(bus_list[0] - T)
else :
  print(-1)