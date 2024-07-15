# https://www.acmicpc.net/problem/1817

n, m = map(int, input().split())
cnt = 0

if n > 0:
  books = list(map(int, input().split()))
  cnt, weight = 1, m
  while books:
    if weight < books[0]:
      weight = m
      cnt += 1
    weight -= books[0]
    books.pop(0)
print(cnt)