# https://www.acmicpc.net/problem/9085

t = int(input())
for _ in range(t) :
    n = int(input())
    nums = list(map(int, input().split()))
    print(sum(nums))