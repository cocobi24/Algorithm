# https://www.acmicpc.net/problem/4435

T = int(input())
for i in range(1, T + 1):
  a, b, c, d, e, f = map(int, input().split())
  A, B, C, D, E, F, G = map(int, input().split())
  team1 = (1 * a) + (2 * b) + (3 * c) + (3 * d) + (4 * e) + (10 * f)
  team2 = (1 * A) + (2 * B) + (2 * C) + (2 * D) + (3 * E) + (5 * F) + (10 * G)

  if team1 > team2:
    ans = "Good triumphs over Evil"
  elif team2 > team1:
    ans = "Evil eradicates all trace of Good"
  else:
    ans = "No victor on this battle field"
  print(f"Battle {i}: {ans}")