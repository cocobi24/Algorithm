# https://www.acmicpc.net/problem/5107

import sys
input = sys.stdin.readline

T_index = 1
while True:
  T = int(input())
  if T == 0:
    break

  name = []
  for _ in range(T):
    a, b = input().split()
    name.append((a,b))

  name_list = []
  for i in range(T):
    flag = False
    for j in range(len(name_list)):
      if (name[i][0] in name_list[j]) or (name[i][1] in name_list[j]):
        name_list[j].append(name[i][1])
        name_list[j].append(name[i][0])
        flag = True
        break
    if not flag:
      name_list.append([])
      name_list[-1].append(name[i][0])
      name_list[-1].append(name[i][1])
  print(T_index, len(name_list))
  T_index += 1