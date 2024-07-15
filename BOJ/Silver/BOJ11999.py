# https://www.acmicpc.net/problem/11999

x, y, m = map(int, input().split())
i = 1

total_list = []
while True :
  temp = []
  for _ in range(i) :
    temp.append(x)
  while sum(temp) < m :
    temp.append(y)
  if sum(temp) > m:
    temp.pop()

  total_list.append(sum(temp))
  if sum(temp) > m :
    total_list.pop()
    break
  i += 1
print(max(total_list))