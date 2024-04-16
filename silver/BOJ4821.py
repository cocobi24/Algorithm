# https://www.acmicpc.net/problem/4821

import sys
input = sys.stdin.readline

while True:
  max_page = int(input())
  if max_page == 0:
    break
  pages = input().rstrip().split(',')
  page_set = set()
  for page in pages:
    if '-' in page:
      low, high = map(int, page.split('-'))
      if low <= high:
        last = 0
        if high <= max_page:
          last = high + 1
        elif low <= max_page:
          last = max_page + 1
        for i in range(low, last):
          page_set.add(i)
    else:
      page = int(page)
      if page <= max_page:
        page_set.add(page)
  print(len(page_set))
