# https://www.acmicpc.net/problem/17211

N, mood = map(int, input().split())
a, b, c, d = map(float, input().split())

p_good, p_bad = (1, 0) if mood == 0 else (0, 1)
for _ in range(N):
  p_good, p_bad = p_good*a + p_bad*c, p_good*b + p_bad*d

print(round(p_good*1000), round(p_bad*1000), sep='\n')