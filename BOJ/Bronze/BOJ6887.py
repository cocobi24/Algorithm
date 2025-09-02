# https://www.acmicpc.net/problem/6887

import math

tiles = int(input())
ans = int(math.sqrt(tiles))
print(f"The largest square has side length {ans}.")