# https://www.acmicpc.net/problem/18186

n, B, C = map(int, input().split())
ramen = list(map(int, input().split())) + [0, 0]
ans = 0
cost_2 = B + C
cost_3 = B + (C * 2)

if B < C:
  print(sum(ramen) * B)
else:
  def sub(option, s):
    global ramen
    if option == 'x':
      ramen[i], ramen[i + 1] = ramen[i] - s, ramen[i + 1] - s
    elif option == 'y':
      ramen[i], ramen[i + 1], ramen[i + 2] = ramen[i] - s, ramen[i + 1] - s, ramen[i + 2] - s

  for i in range(n):
    if ramen[i+1] > ramen[i+2]:
      x = min(ramen[i], ramen[i+1] - ramen[i+2])
      sub('x', x)
      y = min(ramen[i:i+3])
      sub('y', y)
    else:
      y = min(ramen[i:i+3])
      sub('y', y)
      x = min(ramen[i:i+2])
      sub('x', x)
    ans += (x * cost_2) + (y * cost_3) + (ramen[i] * B)

  print(ans)