# https://www.acmicpc.net/problem/25629

n = int(input())
nums = list(map(int, input().split()))
even = list(filter(lambda x:x % 2 == 0, nums))
odd = list(filter(lambda x:x % 2 != 0, nums))
print(1 if len(even) == n//2 else 0)