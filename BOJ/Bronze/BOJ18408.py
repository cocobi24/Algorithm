# https://www.acmicpc.net/problem/18408

nums = list(map(int, input().split()))
print(1 if nums.count(1) >=2 else 2)