# https://www.acmicpc.net/problem/17388

nums = list(map(int, input().split()))
univ = {0: 'Soongsil', 1: 'Korea', 2: 'Hanyang'}
print('OK' if sum(nums) >= 100 else univ[nums.index(min(nums))])