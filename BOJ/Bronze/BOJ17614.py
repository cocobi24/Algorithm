# https://www.acmicpc.net/problem/17614

n = int(input()) + 1
cnt = 0
for i in range(1, n):
  i = str(i)
  cnt += i.count('3')
  cnt += i.count('6')
  cnt += i.count('9')
print(cnt)