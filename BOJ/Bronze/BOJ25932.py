# https://www.acmicpc.net/problem/25932

N = int(input())

def print_anser(list):
  hasZack = 17 in list
  hasMack = 18 in list
  hasBoth = hasZack and hasMack

  if hasBoth:
    print('both')
  elif hasZack:
    print('zack')
  elif hasMack:
    print('mack')
  else:
    print('none')
  print()

for _ in range(N):
  num_list = list(map(int, input().split()))
  print(*num_list)
  print_anser(num_list)