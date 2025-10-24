# https://www.acmicpc.net/problem/5163

import math

K = int(input().strip())
for dataset_num in range(1, K + 1):
  b, w = input().split()
  b = int(b)
  w = float(w)

  total_buoyancy = 0.0
  for _ in range(b):
    r = float(input().strip())
    volume = (4 / 3) * math.pi * r ** 3
    total_buoyancy += volume / 1000

  print(f"Data Set {dataset_num}:")
  print("Yes" if total_buoyancy > w else "No")
  print()