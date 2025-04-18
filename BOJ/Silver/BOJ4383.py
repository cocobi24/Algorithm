# https://www.acmicpc.net/problem/4383

import sys
input = sys.stdin

while True:
    line = input.readline().rstrip().split()
    if not line:
        break
    n = int(line[0])
    nums = list(map(int, line[1:]))
    if n == 1:
        print("Jolly")
        continue

    diff_set = set()
    for i in range(n - 1):
        diff_set.add(abs(nums[i] - nums[i + 1]))
    print("Jolly" if diff_set == set(range(1, n)) else "Not jolly")