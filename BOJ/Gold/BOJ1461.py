# https://www.acmicpc.net/problem/1461

n, m = map(int, input().split())
books = list(map(int, input().split()))

plus, minus = [], []
for i in range(n):
  if books[i] > 0:
    plus.append(books[i])
  else:
    minus.append(abs(books[i]))
plus.sort(reverse=True)
minus.sort(reverse=True)

cnt = 0
for i in range(0, len(plus), m):
  cnt += plus[i] * 2
for i in range(0, len(minus), m):
  cnt += minus[i] * 2

print(cnt - max(abs(max(books)), abs(min(books))))