# https://www.acmicpc.net/problem/2052

n = -int(input())
ans = "%.300f" % 2**n
l = len(ans)
for i in range(l - 1, 1, -1):
  if ans[i] != '0':
    l = i
    break
print(ans[:l + 1])