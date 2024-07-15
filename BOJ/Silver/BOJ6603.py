# https://www.acmicpc.net/problem/6603

import itertools

while True :
    nums = list(map(int, input().split()))

    if nums[0] == 0 :
        break

    del nums[0]
    coms = list(itertools.combinations(nums, 6))
    for com in coms :
        print(*com)
    print()