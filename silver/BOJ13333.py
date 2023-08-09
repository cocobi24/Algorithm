# https://www.acmicpc.net/problem/13333

n = int(input())
num_list = sorted(map(int, input().split()))

def find_k(arr):
  for k in range(n, -1, -1):
    if k <= arr[-k]:
      return k

answer = find_k(num_list)
print(answer)