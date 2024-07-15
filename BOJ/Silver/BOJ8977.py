# https://www.acmicpc.net/problem/8977

n, k, b = map(int, input().split())
nums = list(map(int, input().split()))

def addNumber(x):
  return nums[(x-1) % n]

answer = 0
for i in range(b, b+k):
  answer += addNumber(i)
print(answer)