# https://www.acmicpc.net/problem/33277

n, m = map(int, input().split())
min_day = m / n * 24 * 60
hh = int(min_day // 60)
mm = int(min_day % 60)
print(f'{hh:02d}:{mm:02d}')