# https://www.acmicpc.net/problem/1003

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
nums = sorted([float(input()) * 10 for _ in range(N)])[K:N-K]

nums_sum = sum(nums)
answer_one = nums_sum/(N-2*K) / 10 + 0.00000001
answer_two = (nums_sum + nums[0]*K + nums[-1]*K) / N / 10 + 0.00000001

print('{:.2f}'.format(answer_one))
print('{:.2f}'.format(answer_two))