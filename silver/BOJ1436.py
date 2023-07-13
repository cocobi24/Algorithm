# https://www.acmicpc.net/problem/1436

six_list = []
target = int(input())
n, cnt = 666, 0

while True:
  str_n = str(n)
  if '666' in str_n:
    cnt += 1
  if cnt == target:
    print(n)
    break
  n += 1