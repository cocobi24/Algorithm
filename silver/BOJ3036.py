# https://www.acmicpc.net/problem/3036

import sys
import math
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

for i in range(1,n) :
    gcd = math.gcd(nums[0], nums[i])
    deno = int(nums[0]/gcd)
    num = int(nums[i]/gcd)
    print(F'{deno}/{num}')