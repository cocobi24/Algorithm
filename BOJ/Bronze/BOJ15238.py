# https://www.acmicpc.net/problem/15238

n = int(input())
s = input().rstrip()
unique = set(list(s))
cnt_list = []
for u in unique:
  cnt_list.append([u, s.count(u)])
cnt_list.sort(key=lambda x:(-x[1], x[0]))
print(*cnt_list[0])