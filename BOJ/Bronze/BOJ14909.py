# https://www.acmicpc.net/problem/14909

nums = list(map(int, input().split()))
answer = list(filter(lambda x: x > 0, nums))
print(len(answer))