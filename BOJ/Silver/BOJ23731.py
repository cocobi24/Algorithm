# https://www.acmicpc.net/problem/23731

def solve(n):
  max_val = n
  res = {n}
  current_val = n
  for i in range(1, len(str(n)) + 1):
    power_of_ten = 10 ** i
    remainder = current_val % power_of_ten
    if remainder < power_of_ten / 2:
      current_val -= remainder
    else:
      current_val += (power_of_ten - remainder)

    res.add(current_val)
    max_val = max(max_val, current_val)
  return max(n, max_val)

n = int(input())
ans = solve(n)
print(ans)