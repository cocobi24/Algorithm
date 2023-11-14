# https://www.acmicpc.net/problem/3258

n, z, m = map(int, input().split())
nums = map(int, input().split())

trap = [0] * n
for num in nums:
  trap[num-1] = 1

def solve():
  for k in range(1, z):
    field = [1] + ([0] * (n-1))

    idx = 0
    while True:
      idx += k
      idx %= n
      if idx == z-1:
        print(k)
        return

      if field[idx] or trap[idx]:
        break

solve()