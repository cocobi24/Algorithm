# https://www.acmicpc.net/problem/11257

N = int(input())
std = [35 * 0.3, 25 * 0.3, 40 * 0.3]

for _ in range(N):
  num, s, m, t = map(int, input().split())
  total = s + m + t
  is_pass = total >= 55 \
            and s >= std[0] \
            and m >= std[1] \
            and t >= std[2]
  print(num, total, "PASS" if is_pass else "FAIL")